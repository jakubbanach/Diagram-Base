from ..Diagram import Diagram
import os


class Lifeline:
    name: str
    MIN_LENGTH: int = 200
    BOX_HEIGHT: int = 30
    MIN_BOX_WIDTH: int = 30
    FONT_SIZE: int = 10
    length: int
    x: int

    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.length = self.MIN_LENGTH

    def calculate_box_width(self) -> int:
        return max(self.MIN_BOX_WIDTH, len(self.name) * self.FONT_SIZE) + 10

    def render(self) -> str:
        box_width = self.calculate_box_width()

        return f'\
            <rect fill="none" x="0" width="{box_width}"\n \
                height="{self.BOX_HEIGHT}" y="0" stroke="black" />\n\
            <text fill="black" x="5" y="18"\n\
                text-decoration="underline" stroke="none">{self.name}</text>\n\
            <line x1="{box_width / 2}" x2="{box_width / 2}" \n\
                y1="{self.BOX_HEIGHT}" y2="{self.BOX_HEIGHT + self.length}" \n\
                stroke="gray" />\n'


class Message:
    source: Lifeline
    target: Lifeline
    type_: str  # sync / async / return / create / destroy
    name: str
    x: int
    y: int
    length: int

    def __init__(self, source: Lifeline, target: Lifeline, type_: str, name: str, y: int):
        self.source = source
        self.target = target
        self.type_ = type_
        self.name = name
        self.x = source.x + 30
        self.y = y
        self.length = abs(target.length - source.length)

    def render(self) -> str:
        head = ""
        left_end = self.source.x + self.source.calculate_box_width() // 2
        right_end = self.target.x + self.target.calculate_box_width() // 2
        title_loc = left_end + 5
        line = ""
        line_type = "" 
        #TODO: kierunek ustalania i odległość od Lifeline'u
        match self.type_:
            case "sync":
                head = f'marker-end=\"url(#message_arrow)\"'
                # TODO: kierunek ustalania
                # if right_end>left_end:
                #     right_end -= 10 # cofniecie wyniku
                # else:
                #     left_end -=10
            case "async":
                head = f'marker-end=\"url(#back_message_arrow)\"'                
            case "return":
                head = f'marker-end=\"url(#back_message_arrow)\"'
                line_type = f'stroke-dasharray=\"4 2\"'
                title_loc = right_end + 5
            case "create":
                head = f''
            case "destroy":
                head = f''

        return f'\
            <g transform="translate(0 {self.y})">\n\
                <line fill="none" x1="{left_end}" x2="{right_end}" stroke="black" {head} {line_type}/>\n\
                <text x="{title_loc}" font-size="14" y="-3" fill="black" stroke="none">{self.name}</text>\n\
            </g>\n'


# Later...
#
# class Block:
#     type: str  # alt / opt / loop / par / ... ??
#     messages: list[Message]

#     def __init__(self, type: str):
#         self.type = type
#         self.messages = []

#     def render(self) -> str:
#         # TODO: Implement this method
#         pass


class SequenceDiagram(Diagram):
    lifelines: list[Lifeline]
    messages: list[Message]
    # blocks: list[Block]
    LINE_GAP: int = 300
    MESSAGE_GAP: int = 50
    MARGIN: int = 30

    def __init__(self, name: str):
        super().__init__(name)
        self.lifelines = []
        self.messages = []

    def calculate_width(self) -> int:
        return (len(self.lifelines) - 1) * self.LINE_GAP + (2 * self.MARGIN) + self.lifelines[-1].calculate_box_width()

    def calculate_height(self) -> int:
        return max([lifeline.length for lifeline in self.lifelines]) + (2 * self.MARGIN) + Lifeline.BOX_HEIGHT

    def add_lifeline(self, name: str) -> Lifeline:
        lifeline = Lifeline(name)
        lifeline.x = len(self.lifelines) * self.LINE_GAP
        self.lifelines.append(lifeline)

        return lifeline

    def get_lifeline_by_name(self, name: str) -> Lifeline:
        for lifeline in self.lifelines:
            if lifeline.name == name:
                return lifeline

        raise Exception(f"Lifeline with name '{name}' not found")

    def add_message(self, source: Lifeline, target: Lifeline, type_: str, name: str) -> Message:
        message = Message(source, target, type_, name,
                          self.MARGIN + Lifeline.BOX_HEIGHT + (self.MESSAGE_GAP * len(self.messages)))
        self.messages.append(message)

        return message

    def render(self) -> str:
        result = ""

        result += f'<g transform="translate({self.MARGIN}, {self.MARGIN})">\n'

        for lifeline in self.lifelines:
            result += f'<g transform="translate({lifeline.x}, 0)">\n'
            result += lifeline.render()
            result += "</g>\n"

        for message in self.messages:
            result += message.render()

        result += "</g>\n"

        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "sequence_style.css"), "r") as f:
            style = f.read()

        defs = '<defs>\n\
        <marker id=\"back_message_arrow\" viewBox=\"0 -5 10 10\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto\">\n\
            <path d=\"M 0,-5 L 10,0 L 0,5 Z\" fill=\'white\' stroke=\"black\"/>\n\
        </marker>\n\
        <marker id=\"message_arrow\" viewBox=\"0 -5 10 10\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto\">\n\
            <path d=\"M 0,-5 L 10,0 L 0,5 Z\" fill=\"black\" stroke=\"black\"/>\n\
        </marker>\n</defs>'

        return f'<style type="text/css">\n{style}\n</style>\n{defs}\n{result}'

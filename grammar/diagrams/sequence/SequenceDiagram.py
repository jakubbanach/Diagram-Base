from ..Diagram import Diagram
import os


class Process:
    start: int
    end: int
    offset: int
    WIDTH: int = 16

    def __init__(self, start: int, end: int = None):
        self.start = start
        self.end = end
        self.offset = -self.WIDTH // 2

    def render(self) -> str:
        if self.end is None:
            self.end = self.start + self.WIDTH

        return f'\
                <rect x="{self.offset}" y="{self.start}" fill="white" stroke="black" width="{self.WIDTH}" height="{self.end - self.start}" />\n\
            '


class Lifeline:
    name: str
    MIN_LENGTH: int = 100
    BOX_HEIGHT: int = 30
    MIN_BOX_WIDTH: int = 30
    FONT_SIZE: int = 10
    length: int
    x: int
    processes: list[Process]

    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.length = self.MIN_LENGTH
        self.processes = []

    def activate_at(self, start: int) -> Process:
        process = Process(start)

        i = len(self.processes) - 1
        none_count = 0
        while i >= 0 and self.processes[i].end is None:
            i -= 1
            none_count += 1

        if len(self.processes) > 0 and self.processes[-1].end is None:
            process.offset += none_count * 8

        self.processes.append(process)
        return process

    def deactivate_at(self, end: int) -> Process | None:
        if len(self.processes) > 0:
            activated_process_index = None
            for i, process in enumerate(self.processes[::-1]):
                if process.end is None:
                    activated_process_index = len(self.processes) - i - 1
                    break

            if activated_process_index is None:
                activated_process_index = len(self.processes) - 1

            self.processes[activated_process_index].end = end
            return self.processes[activated_process_index]

    def calculate_box_width(self) -> int:
        return max(self.MIN_BOX_WIDTH, len(self.name) * self.FONT_SIZE) + 10

    def _render_processes(self) -> str:
        for process in self.processes:
            if process.end is None:
                process.end = self.length + self.BOX_HEIGHT - 5

        return f'<g transform="translate({self.calculate_box_width() // 2}, 0)">' + '\n'.join([process.render() for process in self.processes]) + '</g>'

    def render(self) -> str:
        box_width = self.calculate_box_width()

        return f'\
            <rect fill="none" width="{box_width}"\n \
                height="{self.BOX_HEIGHT}" stroke="black" />\n\
            <text fill="black" x="5" y="18"\n\
                text-decoration="underline" stroke="none">{self.name}</text>\n\
            <line x1="{box_width / 2}" x2="{box_width / 2}" \n\
                y1="{self.BOX_HEIGHT}" y2="{self.BOX_HEIGHT + self.length}" \n\
                stroke="gray" />\n\
            {self._render_processes()}\n\
        '


class Message:
    source: Lifeline
    target: Lifeline
    type_: str  # sync / async / return / create / destroy
    name: str
    y: int
    length: int

    def __init__(self, source: Lifeline, target: Lifeline, type_: str, name: str, y: int):
        self.source = source
        self.target = target
        self.type_ = type_
        self.name = name[1:-1]
        self.y = y
        self.length = abs(target.length - source.length)

        if source == target:
            target.activate_at(self.y)
            target.deactivate_at(self.y + 20)
        else:
            match self.type_:
                case "sync":
                    self.target.activate_at(self.y)
                case "async":
                    self.target.activate_at(self.y)
                case "return":
                    self.source.deactivate_at(self.y)
                case "create":
                    pass
                case "destroy":
                    pass
                case _:
                    raise Exception("Unknown message type")

    def render(self) -> str:
        head = ""
        left_end = self.source.x + self.source.calculate_box_width() // 2
        right_end = self.target.x + self.target.calculate_box_width() // 2 - 5
        title_loc = left_end + 5
        line_type = ""

        # TODO: kierunek ustalania i odległość od Lifeline'u
        match self.type_:
            case "sync":
                head = f'marker-end=\"url(#message_arrow)\"'
                if right_end>left_end:
                    right_end -= 15
                else:
                    right_end += 25
            case "async":
                head = f'marker-end=\"url(#back_message_arrow)\"'
                if right_end>left_end:
                    right_end -= 15
                else:
                    right_end += 25
            case "return":
                head = f'marker-end=\"url(#back_message_arrow)\"'
                line_type = f'stroke-dasharray=\"4 2\"'
                if right_end>left_end:
                    right_end -= 15 
                else:
                    right_end += 25
                title_loc = right_end + 5
            case "create":
                # TODO: Na razie zostaw - tu trzeba będzię zrobić trochę więcej
                head = f''
                line_type = f''
            case "destroy":
                # TODO: Tu też
                head = f''
                line_type = f''

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

        return None

    def add_message(self, source: Lifeline, target: Lifeline, type_: str, name: str) -> Message:
        message = Message(source, target, type_, name,
                          self.MARGIN + Lifeline.BOX_HEIGHT + (self.MESSAGE_GAP * len(self.messages)))

        for i, lifeline in enumerate(self.lifelines):
            self.lifelines[i].length = max(
                Lifeline.MIN_LENGTH, message.y - Lifeline.BOX_HEIGHT + self.MESSAGE_GAP // 2)

        self.messages.append(message)

        return message

    def render(self) -> str:
        result = ""

        result += f'<g transform="translate({self.MARGIN}, {self.MARGIN})">\n'

        for i, lifeline in enumerate(self.lifelines):
            self.lifelines[i].length = self.calculate_height(
            ) - (2 * self.MARGIN) - Lifeline.BOX_HEIGHT
            result += f'<g transform="translate({lifeline.x}, 0)">\n'
            result += lifeline.render()
            result += "</g>\n"

        for message in self.messages:
            result += message.render()

        result += "</g>\n"

        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "sequence_style.css"), "r") as f:
            style = f.read()

        defs = '\
            <defs>\n\
                <marker id=\"back_message_arrow\" viewBox=\"0 -5 10 10\" markerWidth=\"10\" markerHeight=\"10\" orient=\"auto\">\n\
                    <path d=\"M 0,-5 L 10,0 L 0,5 Z\" fill=\'white\' stroke=\"black\"/>\n\
                </marker>\n\
                <marker id=\"message_arrow\" viewBox=\"0 -5 10 10\" markerWidth=\"10\" markerHeight=\"10\" orient=\"auto\">\n\
                    <path d=\"M 0,-5 L 10,0 L 0,5 Z\" fill=\"black\" stroke=\"black\"/>\n\
                </marker>\n\
            </defs>\
        '

        return f'<style type="text/css">\n{style}\n</style>\n{defs}\n{result}'

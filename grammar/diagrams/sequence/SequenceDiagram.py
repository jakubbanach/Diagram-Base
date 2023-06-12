from ..Diagram import Diagram
import os


class Lifeline:
    name: str
    MIN_LENGTH: int = 200
    BOX_HEIGHT: int = 30
    BOX_WIDTH: int = 100
    length: int
    x: int

    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.length = self.MIN_LENGTH

    def render(self) -> str:
        return f'\
            <rect fill="none" x="0" width="{self.BOX_WIDTH}" \
                height="{self.BOX_HEIGHT}" y="0" stroke="black" />\
            <text fill="black" x="5" y="18"\
                text-decoration="underline" stroke="none">{self.name}</text>\
            <line x1="{self.BOX_WIDTH / 2}" x2="{self.BOX_WIDTH / 2}" \
                y1="{self.BOX_HEIGHT}" y2="{self.BOX_HEIGHT + self.length}" \
                stroke="gray" />\
            '


class Message:
    source: Lifeline
    target: Lifeline
    type_: str  # sync / async / return / create / destroy ...??
    name: str

    def __init__(self, source: Lifeline, target: Lifeline, type_: str, name: str):
        self.source = source
        self.target = target
        self.type_ = type_
        self.name = name

    def render(self) -> str:
        # TODO: Implement this method
        pass


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
    GAP: int = 300
    MARGIN: int = 30

    def __init__(self, name: str):
        super().__init__(name)
        self.lifelines = []
        self.messages = []

    def calculate_width(self) -> int:
        return (len(self.lifelines) - 1) * self.GAP + (2 * self.MARGIN) + Lifeline.BOX_WIDTH

    def calculate_height(self) -> int:
        return max([lifeline.length for lifeline in self.lifelines])

    def add_lifeline(self, name: str) -> Lifeline:
        lifeline = Lifeline(name)
        lifeline.x = len(self.lifelines) * self.GAP
        self.lifelines.append(lifeline)

        return lifeline

    def render(self) -> str:
        result = ""

        result += f'<g transform="translate({self.MARGIN}, {self.MARGIN})">\n'

        for lifeline in self.lifelines:
            result += f'<g transform="translate({lifeline.x}, 0)">\n'
            result += lifeline.render()
            result += "</g>\n"

        result += "</g>\n"

        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "sequence_style.css"), "r") as f:
            style = f.read()

        return f'<style type="text/css">\n{style}\n</style>\n{result}'

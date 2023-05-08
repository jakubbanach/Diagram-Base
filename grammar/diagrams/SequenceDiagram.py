from .Diagram import Diagram


class Lifeline:
    name: str

    def __init__(self, name: str):
        self.name = name

    def draw(self):
        # TODO: Implement this method
        pass


class Message:
    source: Lifeline
    target: Lifeline
    type: str # sync / async / return / create / destroy ...??
    name: str

    def __init__(self, source: Lifeline, target: Lifeline, type: str, name: str):
        self.source = source
        self.target = target
        self.type = type
        self.name = name

    def draw(self):
        # TODO: Implement this method
        pass


# ???
class Block:
    type: str # alt / opt / loop / par / ... ??
    messages: list[Message]

    def __init__(self, type: str):
        self.type = type
        self.messages = []

    def draw(self):
        # TODO: Implement this method
        pass


class SequenceDiagram(Diagram):
    lifelines: list[Lifeline]
    messages: list[Message]
    blocks: list[Block]

    def __init__(self, name: str):
        super().__init__(name)
        self.actors = []
        self.messages = []

    def draw(self):
        # TODO: Implement this method
        pass

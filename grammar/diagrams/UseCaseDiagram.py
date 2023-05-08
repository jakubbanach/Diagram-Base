from .Diagram import Diagram


class Actor:
    name: str

    def __init__(self, name: str):
        self.name = name

    def draw(self):
        # TODO: Implement this method
        pass


class UseCase:
    name: str

    def __init__(self, name: str):
        self.name = name

    def draw(self):
        # TODO: Implement this method
        pass


class UseCaseAssociation:
    actor: Actor
    use_case: UseCase

    def __init__(self, actor: Actor, use_case: UseCase):
        self.actor = actor
        self.use_case = use_case

    def draw(self):
        # TODO: Implement this method
        pass


class UseCaseRelation:
    source: UseCase
    target: UseCase
    type: str # include / extend

    def __init__(self, source: UseCase, target: UseCase, type: str):
        self.source = source
        self.target = target
        self.type = type

    def draw(self):
        # TODO: Implement this method
        pass


class UseCaseDiagram(Diagram):
    actors: list[Actor]
    use_cases: list[UseCase]
    associations: list[UseCaseAssociation]
    case_relations: list[UseCaseRelation]

    def __init__(self, name: str):
        super().__init__(name)
        self.actors = []
        self.use_cases = []
        self.relations = []

    def draw(self):
        # TODO: Implement this method
        pass
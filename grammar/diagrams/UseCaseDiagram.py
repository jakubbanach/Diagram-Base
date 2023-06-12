from .Diagram import Diagram


class Actor:
    name: str

    def __init__(self, name: str):
        self.name = name

    def render(self) -> str:
        # TODO: Implement this method
        pass


class UseCase:
    name: str

    def __init__(self, name: str):
        self.name = name

    def render(self) -> str:
        # TODO: Implement this method
        pass


class UseCaseAssociation:
    actor: Actor
    use_case: UseCase

    def __init__(self, actor: Actor, use_case: UseCase):
        self.actor = actor
        self.use_case = use_case

    def render(self) -> str:
        # TODO: Implement this method
        pass


class UseCaseRelation:
    source: UseCase
    target: UseCase
    type: str  # include / extend

    def __init__(self, source: UseCase, target: UseCase, type: str):
        self.source = source
        self.target = target
        self.type = type

    def render(self) -> str:
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

    def calcualte_width(self) -> int:
        return 0

    def calculate_height(self) -> int:
        return 0

    def render(self) -> str:
        # TODO: Implement this method
        pass

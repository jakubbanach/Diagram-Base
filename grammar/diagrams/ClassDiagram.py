from .Diagram import Diagram


class UMLClassMethodArgument:
    name: str
    type: str

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def draw(self):
        # TODO: Implement this method
        pass


class UMLClassMethod:
    name: str
    visibility: str
    type: str
    arguments: list[UMLClassMethodArgument]

    def __init__(self, name: str, visibility: str, type: str):
        self.name = name
        self.visibility = visibility
        self.type = type

    def draw(self):
        # TODO: Implement this method
        pass


class UMLClassAttribute:
    name: str
    visibility: str
    type: str

    def __init__(self, name: str, visibility: str, type: str):
        self.name = name
        self.visibility = visibility
        self.type = type

    def draw(self):
        # TODO: Implement this method
        pass


class UMLClass:
    name: str
    attributes: list[UMLClassAttribute]
    methods: list[UMLClassMethod]
    type: str # np. interface, abstract, class

    def __init__(self, name: str):
        self.name = name
        self.attributes = []
        self.methods = []

    def draw(self):
        # TODO: Implement this method
        pass


class UMLEnum:
    name: str
    values: list[str]

    def __init__(self, name: str):
        self.name = name
        self.values = []

    def draw(self):
        # TODO: Implement this method
        pass


class UMLRelation:
    source: UMLClass | UMLEnum
    target: UMLClass | UMLEnum
    type: str # np. association, aggregation, composition, inheritance

    def __init__(self, source: str, target: str, type: str):
        self.source = source
        self.target = target
        self.type = type

    def draw(self):
        # TODO: Implement this method
        pass


class ClassDiagram(Diagram):
    classes: list[UMLClass | UMLEnum]
    relations: list[UMLRelation]

    def __init__(self, name: str):
        super().__init__(name)
        self.classes = []

    def draw(self):
        super().draw()
        # TODO: Implement this method

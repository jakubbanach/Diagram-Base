from ..Diagram import Diagram
from .UMLCLass import UMLClass
from .UMLRelation import UMLRelation


class ClassDiagram(Diagram):
    MARGIN: int = 30
    GAP: int = 240
    classes: list[UMLClass]
    relations: list[UMLRelation]

    def __init__(self, name: str):
        super().__init__(name)
        self.classes = []
        self.relations = []

    def add_class(self, uml_class: UMLClass):
        self.classes.append(uml_class)

    def add_relation(self, relation: UMLRelation):
        self.relations.append(relation)

    def get_last_class(self) -> UMLClass:
        return self.classes[-1]
    
    def _place_classes(self):
        for i, uml_class in enumerate(self.classes):
            uml_class.x = i * (self.GAP + uml_class.WIDTH)
            uml_class.y = 0

    def render(self) -> str:
        result = super().render()

        self._place_classes()

        result += f'<g transform="translate({self.MARGIN} {self.MARGIN})">\n'

        for uml_class in self.classes:
            result += uml_class.render()

        for relation in self.relations:
            result += relation.render()

        result += '</g>'

        return result 

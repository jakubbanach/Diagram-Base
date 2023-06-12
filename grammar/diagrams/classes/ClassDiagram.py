from ..Diagram import Diagram
from .UMLCLass import UMLClass
from .UMLRelation import UMLRelation
import math


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

    def get_last_relation(self) -> UMLRelation:
        return self.relations[-1]

    def _place_classes(self):
        grid_size = math.ceil(math.sqrt(len(self.classes)))

        for i in range(grid_size):
            for j in range(grid_size):
                index = i * grid_size + j
                if index >= len(self.classes):
                    break

                if i == 0:
                    self.classes[index].y = 0
                else:
                    self.classes[index].y = i * \
                        (self.GAP + self.classes[index-grid_size].get_height())

                self.classes[index].x = j * \
                    (self.GAP + self.classes[index].WIDTH)

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

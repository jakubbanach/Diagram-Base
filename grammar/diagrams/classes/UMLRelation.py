from .UMLCLass import UMLClass


class UMLRelation:
    source_multiplicity: str
    target_multiplicity: str
    source: UMLClass
    target: UMLClass
    type_: str  # np. association, aggregation, composition, inheritance

    def __init__(self, source: str, target: str, type_: str):
        self.source = source
        self.target = target
        self.type_ = type_

    def render(self) -> str:
        # TODO: Implement this method
        pass

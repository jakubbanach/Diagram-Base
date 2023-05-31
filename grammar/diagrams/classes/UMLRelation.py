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

        add = ""
        if(type == 'DEPENDENCY'):
            add = "stroke-dasharray=\"4 2\""
        if(type == 'INHERITANCE'):
            add = ""
        if(type == 'PARTIAL_AGGREGATIO'):
            add = ""
        if(type == 'FULL_AGGREGATION'):
            add = ""
        return f'\
            <g>\
                <line x1="{self.source.x+self.source.WIDTH}" x2="{self.target.x}" y1="{self.source.y}" y2="{self.source.y}" />\
            </g>'

        # DEPENDENCY: '...'; Strzałka PRZERYWANA (dodajemy parametr) stroke-dasharray="4 2" - odcinki o długości 4 jednostek i przerw o długości 2 
        # ASSOCIATION: '--'; - LINIA ZWYKŁA 
        # INHERITANCE_RIGHT: '-->'; marker-end="url(#WZOR)" (bez wypelnienia)
        # PARTIAL_AGGREGATION_RIGHT: '--o'; romb (bez wypelnienia)
        # FULL_AGGREGATION_RIGHT: '--*'; romb (z wypelnieniem)
        # changing left and right direction (zmiana parametrow x1<->x2 and y1<-<y2)
        pass

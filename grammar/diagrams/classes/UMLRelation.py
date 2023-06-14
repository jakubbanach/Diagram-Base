from .UMLCLass import UMLClass


class UMLRelation:
    source_multiplicity: str
    target_multiplicity: str
    source: UMLClass
    target: UMLClass
    type_: str  # np. association, aggregation, composition, inheritance
    inverted: bool

    def __init__(self, source: UMLClass, target: UMLClass = None, type_: str = "", 
                inverted: bool = False, source_multiplicity: str="", 
                target_multiplicity: str=""):
        self.source = source
        self.target = target
        self.type_ = type_
        self.inverted = inverted
        self.source_multiplicity = source_multiplicity
        self.target_multiplicity = target_multiplicity
        if self.target!=None:
            print(self.target.name)

    def render(self) -> str:
        # TODO: Implement this method
        if self.target != None:
            if self.inverted:
                temp = self.source
                self.source = self.target
                self.target = temp

            head = ""  #grot strzalki -> ksztalt i wypelnienie
            line_type = ""  #przerywana czy nie
            match self.type_:
                case "dependency":
                    head = f'<polygon fill="black" points="{self.target.x - 17} 0 {self.target.x - 30} 6 {self.target.x - 30} -6" />'
                case "association":
                    head = f''
                case "partial_aggregation":
                    head = f''
                case "full_aggregation":
                    head = f''
                case "inheritance":
                    head = f''    
            # return f'\
            #     <g>\
            #         <line x1="{self.source.x+self.source.WIDTH}" x2="{self.target.x}" y1="{self.source.y}" y2="{self.source.y}" />\
            #     </g>'

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

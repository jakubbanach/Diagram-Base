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
        # if self.source!=None:
        #     print("Source: " + str(self.source.name))
        # if self.target!=None:
        #     print("Target: " + str(self.target.name))
        # print(self.type_, self.inverted)

    def render(self) -> str:
        # TODO: Implement this method
        orient = 'right'
        if self.target != None and self.source != None:
            print(str(self.source.name), str(self.target.name), end =' ')
            print(self.type_, self.inverted)
            if self.inverted:
                # TODO: zmiana kierunku strzalki
                orient = 'left'
            if self.target.x < self.source.x:
                temp = self.source
                self.source = self.target
                self.target = temp
            
            arrow_head = ""
            line_type = ""  #przerywana czy nie
            match self.type_:
                case "dependency":
                    # arrow_head = f'<polygon fill="black" points="{self.target.x - 17} 0 {self.target.x - 30} 6 {self.target.x - 30} -6" />'
                    arrow_head = f'marker-end=\"url(#white_arrow)\"'
                    line_type = f'stroke-dasharray=\"4 2\"'
                case "partial_aggregation":
                    arrow_head = f'marker-end=\"url(#aggregation_white_arrow)\"'
                case "full_aggregation":
                    arrow_head = f'marker-end=\"url(#aggregation_black_arrow)\"'
                case "inheritance":
                    arrow_head = f'marker-end=\"url(#black_arrow)\"'
            return f'\
                <g>\
                    <line x1="{self.source.x+self.source.WIDTH+15}" x2="{self.target.x - 15}" y1="{self.source.y+self.source.BASE_HEIGHT/2}" y2="{self.target.y+self.target.BASE_HEIGHT/2}" {arrow_head} {line_type}/>\
                </g>'
        else:
            return ""
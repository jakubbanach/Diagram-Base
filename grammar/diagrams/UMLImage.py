from .Diagram import Diagram


class UMLImage:
    BACKGROUND_COLOR: str = "#ffffff"
    width: int
    height: int
    diagram: Diagram
    directory: str

    def __init__(self, diagram: Diagram, directory: str = ""):
        self.width = 1920
        self.height = 1080
        self.diagram = diagram
        self.directory = directory

    def draw(self):
        with open(f"{self.directory}{self.diagram.name}.svg", "w") as f:
            f.write(f'<!DOCTYPE svg>\n\
                    <svg height="{self.height}" width="{self.width}" style="background-color:{self.BACKGROUND_COLOR}">')
            f.write(self.diagram.render())
            f.write("\n</svg>")

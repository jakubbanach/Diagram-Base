from .Diagram import Diagram


class UMLImage:
    BACKGROUND_COLOR: str = "#ffffff"
    diagram: Diagram
    directory: str

    def __init__(self, diagram: Diagram, directory: str = ""):
        self.diagram = diagram
        self.directory = directory

    def _calculate_width(self):
        return self.diagram.calculate_width()

    def _calculate_height(self):
        return self.diagram.calculate_height()

    def draw(self):
        with open(f"{self.directory}{self.diagram.name}.svg", "w") as f:
            f.write(f'<!DOCTYPE svg>\n\
                    <svg xmlns="http://www.w3.org/2000/svg" height="{self._calculate_height()}" width="{self._calculate_width()}" style="background-color:{self.BACKGROUND_COLOR}">')
            f.write(self.diagram.render())
            f.write("\n</svg>")

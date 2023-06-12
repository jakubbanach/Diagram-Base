import os
from abc import ABC, abstractmethod


class Diagram(ABC):
    name: str

    def __init__(self, name: str = "UML"):
        self.name = name

    @abstractmethod
    def calculate_width(self) -> int:
        pass

    @abstractmethod
    def calculate_height(self) -> int:
        pass

    def render(self) -> str:
        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "style.css"), "r") as f:
            style = f.read()

        return f'<style type="text/css">\n{style}\n</style>\n'

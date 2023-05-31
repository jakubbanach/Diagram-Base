import os
from abc import ABC, abstractmethod

class Diagram(ABC):
    name: str

    def __init__(self, name: str = "UML"):
        self.name = name

    def render(self) -> str:
        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "style.css"), "r") as f:
            style = f.read()

        return f'<style type="text/css">\n{style}\n</style>\n'

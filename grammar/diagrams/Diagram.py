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

    @abstractmethod
    def render(self) -> str:
        pass

from ..Diagram import Diagram
import math


class Actor:
    name: str
    x: int
    y: int
    FONT_SIZE = 12
    HEIGHT = 80
    WIDTH = 30

    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.y = 0

    def render(self) -> str:
        return f'<g transform="translate({self.x - 15} {self.y + 30})">\
            <path\
                d="m 0,0,0,41.7649 -13.92164,18.79028 m 13.92164,-18.54025 11.466,15.64351 m -31.02188,-39.24135 39.77164,-13.52236 m -6.12305,-18.98745 c 0,7.7832 -6.30952,14.09272 -14.09271,14.09272 -7.78319,0 -14.09272,-6.30952 -14.09272,-14.09272 0,-7.78319 6.30953,-14.09271 14.09272,-14.09271 7.78319,0 14.09271,6.30952 14.09271,14.09271 z"\
                style="fill:none;stroke:#000000"\
            />\
            <text\
                x="0"\
                y="{self.HEIGHT - 5}"\
                style="font-size:{self.FONT_SIZE}px;text-anchor:middle"\
            >\
                {self.name}\
            </text>\
        </g>'


class UseCase:
    name: str
    text: str
    width: int
    x: int
    y: int
    HEIGHT = 50
    MIN_WIDTH = 70
    FONT_SIZE = 12
    MARGIN = 10

    def __init__(self, name: str, text: str = ""):
        self.name = name
        if text == "":
            self.text = name
        else:
            self.text = text
        self.width = max(self.MIN_WIDTH, self.calculate_width())
        self.x = 0
        self.y = 0

    def calculate_width(self) -> int:
        return 2 * self.MARGIN + self.FONT_SIZE * len(self.name)

    def render(self) -> str:
        return f'<g transform="translate({self.x} {self.y})">\
            <ellipse\
                cx="{self.width // 2}"\
                cy="{self.HEIGHT // 2}"\
                rx="{self.width // 2}"\
                ry="{self.HEIGHT // 2}"\
                style="fill:white;stroke:#000000"\
            />\
            <text\
                x="{self.width // 2}"\
                y="{self.HEIGHT // 2}"\
                style="font-size:{self.FONT_SIZE}px;text-anchor:middle"\
            >\
                {self.text}\
            </text>\
        </g>'


class UseCaseAssociation:
    actor: Actor
    use_case: UseCase

    def __init__(self, actor: Actor, use_case: UseCase):
        self.actor = actor
        self.use_case = use_case

    def render(self) -> str:
        # TODO: Implement this method
        pass


class UseCaseRelation:
    source: UseCase
    target: UseCase
    type_: str  # include / extend

    def __init__(self, source: UseCase, target: UseCase, type_: str):
        self.source = source
        self.target = target
        self.type_ = type_

    def render(self) -> str:
        # TODO: Implement this method
        pass


class Package:
    name: str
    usecases: list[UseCase]
    width: int
    height: int
    MARGIN = 20
    MIN_WIDTH = 100
    MIN_HEIGHT = 80
    FONT_SIZE = 16

    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.y = 0
        self.width = self.MIN_WIDTH
        self.height = self.MIN_HEIGHT
        self.usecases = []

    def add_usecase(self, usecase: UseCase):
        self.usecases.append(usecase)

    def calculate_width(self) -> int:
        return 0

    def calculate_height(self) -> int:
        return 0

    def render(self) -> str:
        pass


class UseCaseDiagram(Diagram):
    actors: list[Actor]
    packages: list[Package]
    use_cases: list[UseCase]
    associations: list[UseCaseAssociation]
    relations: list[UseCaseRelation]
    MARGIN = 30
    ACTORS_SPACE = 100
    ACTORS_GAP = 30
    USECASES_GAP = 60
    MIN_WIDTH = 200
    MIN_HEIGHT = 200

    def __init__(self, name: str):
        super().__init__(name)
        self.actors = []
        self.use_cases = []
        self.relations = []
        self.associations = []
        self.packages = []

    def add_actor(self, name: str):
        self.actors.append(Actor(name))

    def add_usecase(self, name: str, text: str = ""):
        self.use_cases.append(UseCase(name, text))

    def add_relation(self, source: UseCase, target: UseCase, type_: str):
        self.relations.append(UseCaseRelation(source, target, type_))

    def add_association(self, actor: Actor, use_case: UseCase):
        self.associations.append(UseCaseAssociation(actor, use_case))

    def calculate_width(self) -> int:
        width = 2 * self.MARGIN + self.ACTORS_SPACE
        if len(self.actors) > 1:
            width += self.ACTORS_SPACE

        max_package = 0
        if len(self.packages) > 0:
            max_package = max([package.calculate_width()
                              for package in self.packages]) + 2 * Package.MARGIN

        max_usecase = 0
        if len(self.use_cases) < 4:
            max_usecase = max([usecase.calculate_width()
                              for usecase in self.use_cases])
        else:
            max_usecase = max([usecase.calculate_width() for usecase in self.use_cases[0::2]]) + \
                self.USECASES_GAP + max([usecase.calculate_width()
                                        for usecase in self.use_cases[1::2]])

        width += max(max_package, max_usecase)

        return max(self.MIN_WIDTH, width)

    def calculate_height(self) -> int:
        height = 2 * self.MARGIN

        actors_height = math.ceil(len(self.actors) / 2) * \
            (self.ACTORS_GAP + Actor.HEIGHT + Actor.FONT_SIZE) - self.ACTORS_GAP

        usecase_height = 0
        if len(self.use_cases) < 4:
            usecase_height = len(
                self.use_cases) * (self.USECASES_GAP + UseCase.HEIGHT) - self.USECASES_GAP
        else:
            usecase_height = len(self.use_cases) * UseCase.HEIGHT

        height += max(actors_height, usecase_height)

        return max(self.MIN_HEIGHT, height)

    def render(self) -> str:
        result = f'<g transform="translate({self.MARGIN}, {self.MARGIN})">\n'

        for i, actor in enumerate(self.actors):
            if i % 2 == 0:
                actor.x = self.ACTORS_SPACE // 2
            else:
                actor.x = self.calculate_width() - self.ACTORS_SPACE // 2 - Actor.WIDTH

            actor.y = math.floor(i / 2) * (self.ACTORS_GAP +
                                           Actor.HEIGHT + Actor.FONT_SIZE)

            result += actor.render() + "\n"

        for i, use_case in enumerate(self.use_cases):
            if len(self.use_cases) < 4:
                use_case.x = self.ACTORS_SPACE
                use_case.y = i * (self.USECASES_GAP + UseCase.HEIGHT)
            else:
                use_case.x = self.ACTORS_SPACE if i % 2 == 0 else self.ACTORS_SPACE + \
                    self.use_cases[i-1].calculate_width() + self.USECASES_GAP
                use_case.y = i * UseCase.HEIGHT

            result += use_case.render() + "\n"

        for relation in self.relations:
            result += relation.render() + "\n"

        for association in self.associations:
            result += association.render() + "\n"

        result += "</g>\n"

        return result

from .Diagram import Diagram


class UMLClassMethodArgument:
    name: str
    type: str

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def render(self) -> str:
        return f'{self.name}: {self.type}'


class UMLClassMethod:
    name: str
    visibility: str
    type: str
    arguments: list[UMLClassMethodArgument]

    def __init__(self, name: str, visibility: str, type: str):
        self.name = name
        self.visibility = visibility
        self.type = type
        self.arguments = []

    def _render_arguments(self) -> str:
        return ", ".join([arg.render() for arg in self.arguments])

    def render(self, y) -> str:
        return f'\
            <text x="30" y="{y}" class="visibility">{self.visibility}</text>\
            <text x="60" y="{y}" class="item">{self.name}({self._render_arguments()}): {self.type}</text>\
        '


class UMLClassField:
    name: str
    visibility: str
    type: str

    def __init__(self, name: str, visibility: str, type: str):
        self.name = name
        self.visibility = visibility
        self.type = type

    def render(self, y) -> str:
        return f'\
            <text x="30" y="{y}" class="visibility">{self.visibility}</text>\
            <text x="60" y="{y}" class="item">{self.name}: {self.type}</text>\
        '


class UMLClass:
    name: str
    x: int
    y: int
    WIDTH: int = 320

    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y


class UMLBasicClass(UMLClass):
    fields: list[UMLClassField]
    methods: list[UMLClassMethod]
    base_height: int = 90

    def __init__(self, name: str, x: int = 0, y: int = 0):
        super().__init__(name, x, y)
        self.fields = []
        self.methods = []

    def add_field(self, field: UMLClassField):
        self.fields.append(field)

    def add_method(self, method: UMLClassMethod):
        self.methods.append(method)

    def _render_fields(self) -> str:
        return [field.render((i+1)*35 + self.base_height - 15) for i, field in enumerate(self.fields)]
    
    def _render_methods(self) -> str:
        return [method.render((i+1)*35 + self.base_height - 15 + len(self.fields * 35)) for i, method in enumerate(self.methods)]

    def render(self) -> str:
        height = self.base_height + len(self.fields) * \
            35 + len(self.methods) * 35

        return f'\
            <g transform="translate({self.x},{self.y})">\
                <rect width="{self.WIDTH}" height="{height}" />\
                <line x1="0" x2="320" y1="60" y2="60" />\
                <line x1="0" x2="320" y1="80" y2="80" />\
                <text x="160" y="45" class="name">{self.name}</text>\
                {self._render_fields()}\
                {self._render_methods()}\
            </g>'


class UMLAbstractClass(UMLBasicClass):
    base_height: int = 125

    def __init__(self, name: str, x: int = 0, y: int = 0):
        super().__init__(name, x, y)

    def render(self) -> str:
        height = self.base_height + len(self.fields) * \
            35 + len(self.methods) * 35

        return f'\
            <g transform="translate({self.x},{self.y})">\
                <rect width="{self.WIDTH}" height="{height}" />\
                <line x1="0" x2="320" y1="95" y2="95" />\
                <line x1="0" x2="320" y1="115" y2="115" />\
                <text x="160" y="45" class="name">«Abstract»</text>\
                <text x="160" y="80" class="name">{self.name}</text>\
                {self._render_fields()}\
                {self._render_methods()}\
            </g>'


class UMLInterface(UMLBasicClass):
    base_height: int = 125

    def __init__(self, name: str, x: int = 0, y: int = 0):
        super().__init__(name, x, y)

    def render(self) -> str:
        base_height = 125
        height = base_height + len(self.fields) * \
            35 + len(self.methods) * 35

        return f'\
            <g transform="translate({self.x},{self.y})">\
                <rect width="{self.WIDTH}" height="{height}" />\
                <line x1="0" x2="320" y1="95" y2="95" />\
                <line x1="0" x2="320" y1="115" y2="115" />\
                <text x="160" y="45" class="name">«Interface»</text>\
                <text x="160" y="80" class="name">{self.name}</text>\
                {self._render_fields()}\
                {self._render_methods()}\
            </g>'


class UMLEnumField:
    name: str

    def __init__(self, name: str):
        self.name = name

    def render(self, y) -> str:
        return f'<text x="60" y="{y}" class="item">{self.name}</text>'


class UMLEnum(UMLClass):
    fields: list[UMLEnumField]

    def __init__(self, name: str, x: int = 0, y: int = 0):
        super().__init__(name, x, y)
        self.name = name
        self.fields = []

    def add_field(self, value: UMLEnumField):
        self.fields.append(value)

    def render(self) -> str:
        base_height = 125
        height = base_height + len(self.fields) * 35

        return f'\
            <g transform="translate({self.x},{self.y})">\
                <rect width="{self.WIDTH}" height="{height}" />\
                <line x1="0" x2="320" y1="95" y2="95" />\
                <line x1="0" x2="320" y1="115" y2="115" />\
                <text x="160" y="45" class="name">«Enumeration»</text>\
                <text x="160" y="80" class="name">{self.name}</text>\
                {[field.render((i+1)*35 + base_height - 15) for i, field in enumerate(self.fields)]}\
            </g>'


class UMLRelation:
    source_multiplicity: str
    target_multiplicity: str
    source: UMLClass
    target: UMLClass
    type: str  # np. association, aggregation, composition, inheritance

    def __init__(self, source: str, target: str, type: str):
        self.source = source
        self.target = target
        self.type = type

    def render(self) -> str:
        # TODO: Implement this method
        pass


class ClassDiagram(Diagram):
    classes: list[UMLClass]
    relations: list[UMLRelation]

    def __init__(self, name: str):
        super().__init__(name)
        self.classes = []
        self.relations = []

    def add_class(self, uml_class: UMLClass):
        self.classes.append(uml_class)

    def add_relation(self, relation: UMLRelation):
        self.relations.append(relation)

    def get_last_class(self) -> UMLClass:
        return self.classes[-1]

    def render(self) -> str:
        return super().render() + f'\
            {[uml_class.render() for uml_class in self.classes]}\
        '
        # {[relation.render() for relation in self.relations]}\

class Model(object):
    def __init__(self, name=None, extends=None, properties=None, id=None, description=None):
        self._name = name
        self._extends = extends
        self._properties = properties
        self._id = id
        self._description = description

    def __repr__(self):
        return '<Model object \'{name}\'>'.format(name=self.name)

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self):
        return self._name

    @property
    def extends(self):
        if self._extends == '':
            return None
        return self._extends

    @property
    def properties(self):
        return self._properties

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

class Property(object):

    def __init__(self, name, type=None, ref=None, description=None, items=None):
        self._name = name
        self._type = type
        self._ref = ref
        self._description = description
        self._items = items

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def ref(self):
        return self._ref

    @property
    def description(self):
        return self._description

    @property
    def items(self):
        return self._items

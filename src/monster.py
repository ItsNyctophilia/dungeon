from entity import Entity


class Monster(Entity):
    def __init__(self, name, description):
        super().__init__()
        self._name = name
        self._description = description

    def __str__(self):
        return f'{self._name}: {self._description}'

    @property
    def name(self):
        """Returns the name of the Monster"""
        return f'{self._name}'

    @property
    def description(self):
        """Returns the description of the Monster"""
        return self._description

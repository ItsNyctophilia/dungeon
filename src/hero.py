from .entity import Entity


class Hero(Entity):
    """Hero Class"""
    def __init__(self):
        super().__init__()
        self._hp = 10
        self._dice = 3

    def __str__(self):
        treasures = []
        for selection in enumerate(self._treasure):
            treasures.append(f"{selection}")
        return f'{self._hp}, {treasures}'

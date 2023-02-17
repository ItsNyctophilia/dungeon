class Room:
    def __init__(self, description, num_foes=-1):
        self._description = description
        self._num_foes = num_foes
        self._treasure = []

    def __str__(self):
        return f"{self._description}\n{self._num_foes}\n{self._treasure}"

    @property
    def description(self):
        """World-building description of the room"""
        return self._description

    @property
    def num_foes(self):
        """Number of enemies remaining in the room"""
        return self._num_foes

    @num_foes.setter
    def num_foes(self, num_foes):
        self._num_foes = num_foes

    @property
    def treasure(self):
        """List of the treasure items found in the room"""
        return self._treasure

    @treasure.setter
    def treasure(self, treasure):
        self._treasure = treasure

    def add_treasure(self, new_treasure):
        """Add the given treasure to the room"""
        self._treasure.append(new_treasure)

    def del_treasure(self, treasure):
        """Remove the given treasure from the room"""
        self._treasure.remove(treasure)


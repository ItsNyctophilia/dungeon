from .treasure import Treasure


class Entity:
    def __init__(self):
        self._hp = 0
        self._dice = 0
        self._treasure = {}

    def __str__(self):
        return f'{self._hp}, {self._dice}'

    @property
    def hp(self):
        """Set the health to the specified value"""
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        """Set the health to the specified value"""
        self._hp = new_hp

    @property
    def dice(self):
        """Set the amount of dice to the specified value"""
        return self._dice

    @dice.setter
    def dice(self, num_of_dice):
        """Set the amount of dice to the specified value"""
        self._dice = num_of_dice

    @property
    def treasure(self):
        """Treasure held by an entity"""
        return self._treasure

    def add_treasure(self, treasure):
        """Add a treasure object to an entity's inventory.

        Returns True if successful and False if the action failed
        as a result of the object not being a Treasure."""
        if not isinstance(treasure, Treasure):
            return False
        elif treasure.name in self._treasure.keys():
            count = self._treasure[treasure.name] + 1
            self._treasure.update({treasure.name: count})
        else:
            self._treasure.setdefault(treasure.name, 1)
        return True

    def del_treasure(self, treasure):
        """Remove a treasure from an entity's inventory

        Returns True if successful or if the item was not found
        inside of the dictionary and False if the action failed
        as a result of the object not being a Treasure."""
        if not isinstance(treasure, Treasure):
            return False
        self._treasure.pop(treasure.name, None)
        return True

    def hit(self):
        """Decrement HP if attack lands"""
        self._hp -= 1

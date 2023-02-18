"""Create "Entity" objects that have hp, dice, and inventories.

Contains methods for the getting and setting of hp and dice values
as well as the addition of, removal of, state-checking of, and
pretty-printing of the Entity's inventory."""

from .treasure import Treasure


class Entity:
    """A class to represent a living entity.

    Attributes
    ----------
    hp : int
        health of an entity
    dice : int
        number of dice entity rolls in combat
    treasure : dict
        entity's inventory containing treasure objects

    Methods
    -------
    get_treasure_printout():
        returns a formatted string of the inventory
    add_treasure(treasure):
        adds the given treasure object to the inventory
    del_treasure(treasure):
        removes the given treasure object from the inventory
    has_treasure(treasure):
        checks if treasure object exists in inventory
    hit():
        subtracts 1 hp from entity's helath"""

    def __init__(self):
        self._hp = 0
        self._dice = 0
        self._treasure = {}

    def __str__(self):
        return f'{self._hp}, {self._dice}, {self._treasure}'

    @property
    def hp(self):
        """The amount of health a given entity has"""
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        """Set the health to the specified value"""
        self._hp = new_hp

    @property
    def dice(self):
        """The amount of dice a given entity rolls during combat"""
        return self._dice

    @dice.setter
    def dice(self, num_of_dice):
        """Set the amount of dice to the specified value"""
        self._dice = num_of_dice

    @property
    def treasure(self):
        """Treasure held by an entity"""
        return self._treasure

    def get_treasure_printout(self):
        """Returns a formatted string of the entity's inventory"""
        printout = []

        # "Format: [number]x [item], [description]\n"
        # Ex. "1x Sword of Swording, It looks very sharp."
        for item in self._treasure:
            printout.append("".join([str(self._treasure[item][0]),
                            "x ", item, ", ", self._treasure[item][1]]))
        return "\n".join(printout)

    def add_treasure(self, treasure):
        """Add a treasure object to an entity's inventory.

        Returns True if successful and False if the action failed
        as a result of the object not being a Treasure."""
        if not isinstance(treasure, Treasure):
            return False
        elif treasure.name in self._treasure.keys():
            # _treasure is a dictionary where the values are the
            # number of instances an entity has of a given treasure
            # and the description of that item, in a list
            count = self._treasure[treasure.name][0] + 1
            self._treasure.update({treasure.name:
                                   [count, treasure.description]})
        else:
            self._treasure.setdefault(treasure.name,
                                      [1, treasure.description])
        return True

    def del_treasure(self, treasure):
        """Remove a treasure from an entity's inventory.

        Returns True if successful or if the item was not found
        inside of the dictionary and False if the action failed
        as a result of the object not being a Treasure."""
        if not isinstance(treasure, Treasure):
            return False
        self._treasure.pop(treasure.name, None)
        return True

    def has_treasure(self, treasure_name):
        """Checks if the entity's inventory contains the treasure.

        Returns True if successful or if the item was not found
        inside of the dictionary and False if the action failed
        as a result of the object not being a Treasure."""
        if treasure_name in self._treasure.keys():
            return True
        return False

    def hit(self):
        """Decrement hp by one.

        For use during game combat when attack lands."""
        self._hp -= 1

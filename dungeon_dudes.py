#!/usr/bin/env python3

import random


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


class Menu:
    def __init__(self):
        self._selections = []

    def __str__(self):
        """Return a string of the printout of sorted menu options"""
        menu_string = []
        for idx, selection in enumerate(sorted(self._selections), start=1):
            menu_string.append(f"{idx}. {selection}")
        return "\n".join(menu_string)

    @property
    def selections(self):
        """One of the selectable options in a menu"""
        return self._selections

    def has_selection(self, selection):
        """Return True if selection is in menu, else False"""
        return True if self._selections.count(selection) > 0 else False

    def add_selection(self, new_selection):
        """Add the given selection to the menu"""
        self._selections.append(new_selection)

    def del_selection(self, selection):
        """Remove the given selection from the menu"""
        self._selections.remove(selection)


def main():
    m = Menu()
    m.add_selection("Inventory")
    m.add_selection("Explore")
    m.add_selection("Status")
    m.add_selection("Sense")
    m.add_selection("Attack")
    print(m)

    r = Room("This is a placeholder.", 20)
    print(r)


if __name__ == "__main__":
    try:
        main()
    except (Exception, GeneratorExit, KeyboardInterrupt, SystemExit) as e:
        name = type(e).__name__
        print("Exception of type", name, "prevented program from continuing!")

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


def generate_room(num_foes=-1):
    """Randomly generates a room object to be explored by the player

    Keyword arguments:
    num_foes -- an optional number of enemies for the room

    Returns a room object."""
    random.seed()
    description = "This is a placeholder."
    # TODO: create a description-generation function
    if num_foes == -1:
        num_foes = random.randint(0, 3)
    room = Room(description, num_foes)
    return room


def main():

    main_menu = Menu()
    main_menu.add_selection("Inventory")
    main_menu.add_selection("Explore")
    main_menu.add_selection("Status")

    room = generate_room(0)
    while (True):
        print(
            "You find yourself in a place that can be described as such:\n",
            room.description, "\n", main_menu, sep="")
        choice = input("> ")
        choice = choice.lower().strip()
        # TODO: check if num_enemies > 0
        # TODO: resolve_combat()
        if choice == "inventory":
            print("Placeholder loot bag")
        elif choice == "explore":
            room = generate_room()
            continue
        elif choice == "status":
            print("Placeholder health value")
        else:
            print("Unrecognized command")


if __name__ == "__main__":
    try:
        main()
    except (Exception, GeneratorExit, KeyboardInterrupt, SystemExit) as e:
        name = type(e).__name__
        print("Exception of type", name, "prevented program from continuing!")

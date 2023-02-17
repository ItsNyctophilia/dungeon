#!/usr/bin/env python3

import src.room
from src.menu import Menu
from src.entity import Entity
from src.monster import Monster

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

    main_menu = Menu()
    main_menu.add_selection("Inventory")
    main_menu.add_selection("Explore")
    main_menu.add_selection("Status")

    # ip == "introductory prompt"
    ip = "You awaken in a dark thicket, choked by overgrowth and drowned " \
         "in swampwater. Mosquitos incessantly bite you through your " \
         "clothes and your boots are already waterlogged. The only source " \
         "of light comes from a torch twenty or so paces in the distance, " \
         "roaring strong with a flame that refuses to die in spite of the " \
         "rainwater dripping from the canopy above. Seeing no other " \
         "option, you bring yourself forward and grab ahold of it, " \
         "beginning your journey out of this blackened bog."
    print(src.room.create_description_line(ip, src.room.get_flavor_line()),
          main_menu, sep="")

    while (True):
        choice = input("> ")
        choice = choice.lower().strip()
        # TODO: check if num_enemies > 0
        # TODO: resolve_combat()
        if choice == "inventory":

            print("Placeholder loot bag")

        elif choice == "explore":

            room = src.room.generate_room()
            print(src.room.create_description_line(
                  room.description, src.room.get_flavor_line()),
                  main_menu, sep="")
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

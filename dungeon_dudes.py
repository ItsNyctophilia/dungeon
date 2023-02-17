#!/usr/bin/env python3


class Menu:
    def __init__(self):
        self._selections = []

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


if __name__ == "__main__":
    try:
        main()
    except (Exception, GeneratorExit, KeyboardInterrupt, SystemExit) as e:
        name = type(e).__name__
        print("Exception of type", name, "prevented program from continuing!")

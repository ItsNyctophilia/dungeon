#!/usr/bin/env python3

from src.menu import Menu
from src.entity import Entity
from src.monster import Monster


def main():
    m = Menu()
    m.add_selection("Inventory")
    m.add_selection("Explore")
    m.add_selection("Status")
    m.add_selection("Sense")
    m.add_selection("Attack")
    print(m)

    test = Entity()
    test.hp = 100
    test.dice = 5
    print(test)

    monster = Monster("Beholder", "Giant Eyeball")
    monster.hp = 10
    monster.dice = 3
    print(monster)


if __name__ == "__main__":
    try:
        main()
    except (Exception, GeneratorExit, KeyboardInterrupt, SystemExit) as e:
        name = type(e).__name__
        print("Exception of type", name, "prevented program from continuing!")

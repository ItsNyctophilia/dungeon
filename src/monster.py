"""Create "Monster" objects that contain combat stats and descriptions

Contains Monster class for the creation of entities that require
names and descriptions. Contains method for generation of monster
based on select input files."""

import random
import textwrap
import os
from .entity import Entity


class Monster(Entity):
    """A class to represent an attackable monster.

    Attributes
    ----------
    name : str
        monster's name
    description : str
        monster's description

    Methods
    -------
    generate_monster():
        randomly selects a monster from input file for use in game"""

    def __init__(self, name, description):
        super().__init__()
        self._name = name
        self._description = description

    def __str__(self):
        return f'{self._name}: {self._description}\n HP:{self._hp}'

    @property
    def name(self):
        """Returns the name of the Monster"""
        return f'{self._name}'

    @property
    def description(self):
        """Returns the description of the Monster"""
        return self._description

    @staticmethod
    def generate_monster():
        """Generate monster based on input file in user's home

        Returns a monster object after reading either the user's
        monster file or the program default one in src if that one
        was not found."""

        random.seed()
        home_directory = os.path.expanduser('~')
        path = os.path.join(home_directory, '.dd_monsters')
        try:
            with open(path) as file:
                file.readline()
                lines = file.readlines()
        except FileNotFoundError:
            print("\nCould not find monster file in home directory!")
            print("Reading .dd_monsters in src folder.\n")
            with open("src/.dd_monsters") as file:
                file.readline()
                lines = file.readlines()
        
        if len(lines) == 0:
            print("Empty Monster File. Could not generate a monster!")
            return -1

        index = random.randint(0, len(lines)-1)
        checker = 0
        while True:
            try:
                name, description, hp, dice = lines[index].rstrip().split(";")
                hp = int(hp)
                dice = int(dice)
                break
            except ValueError:
                # ignore the line
                if checker == len(lines):
                    print("No Valid Monsters in the Monster File!")
                    return -1
                checker += 1
                index = random.randint(0, len(lines)-1)
                continue

        monster = Monster(name, textwrap.fill(description).strip("\" "))
        monster._hp = hp
        monster._dice = dice
        return monster

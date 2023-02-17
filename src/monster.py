import random
import os
from .entity import Entity


class Monster(Entity):
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
        random.seed()
        # TODO: Change to read from Home Directory.
        home_directory = os.path.expanduser('~')
        path = os.path.join(home_directory, '.dd_monsters')
        with open(path) as file:
            file.readline()
            lines = file.readlines()

        index = random.randint(0, len(lines)-1)
        name, description, hp, dice = lines[index].rstrip().split(";")
        hp = int(hp)
        dice = int(dice)

        monster = Monster(name, description)
        monster._hp = hp
        monster._dice = dice
        return monster

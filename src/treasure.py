import random


class Treasure:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __str__(self):
        return f'{self._name}, {self._description}'

    @property
    def name(self):
        """The name of a treasure item"""
        return self._name

    @property
    def description(self):
        """Description of a treasure item"""
        return self._description


def get_treasure():
    # TODO: change these descriptions
    t1 = ["Hat of hatting", "Hats hats really hattily."]
    t2 = ["Sword of swashbuckling", "Goes swoosh. Wow!"]
    t3 = ["Boots of running really fast", "Infinite mobility."]
    t4 = ["A bag of gold", "Disrespect monsters, acquire currency"]
    t5 = ["Buckner's buckler", "You assume this belongs to Buckner"]
    treasures = [t1, t2, t3, t4, t5]
    selected_treasure = random.choice(treasures)
    return Treasure(selected_treasure[0], selected_treasure[1])

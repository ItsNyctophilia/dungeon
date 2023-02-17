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
    t1 = ["Attack Potion", "A crimson draught that swirls with energy."]
    t2 = ["Tarnished Heirloom", "A relic of some royal family lost to time."]
    t3 = ["Waterlogged Boot", "Not much dryer than the ones you have on."]
    t4 = ["Sack of Coins", "You won't find much use for money out here."]
    t5 = ["Rusted Weapon", "An implement of war showing signs of wear."]
    t6 = ["Timber", "Dry wood is a rare thing to find in this damp bog."]
    treasures = [t1, t2, t3, t4, t5, t6]
    selected_treasure = random.choice(treasures)
    return Treasure(selected_treasure[0], selected_treasure[1])

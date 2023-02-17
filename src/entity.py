class Entity:
    def __init__(self):
        self._hp = 0
        self._dice = 0
        self._treasure = []

    def __str__(self):
        return f'{self._hp}, {self._dice}'

    @property
    def hp(self):
        """Set the health to the specified value"""
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        """Set the health to the specified value"""
        self._hp = new_hp

    @property
    def dice(self):
        """Set the amount of dice to the specified value"""
        return self._dice

    @dice.setter
    def dice(self, num_of_dice):
        """Set the amount of dice to the specified value"""
        self._dice = num_of_dice

    def treasure(self, treasure):
        """Add a treasure to the list"""
        self._treasure.append(treasure)

    def hit(self):
        """Decrement HP if attack lands"""
        self._hp -= 1

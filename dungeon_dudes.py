#!/usr/bin/env python3

import random
import textwrap


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


def get_description():
    p1 = "As you trudge onwards, enduring the scrapes of brambled " \
         "overgrowth and pushing past the ruins of buildings lost to " \
         "time, you can feel a gentle rain coming from overhead. Just " \
         "above you, the thicket breaks just enough to let several wisps" \
         " of light illuminate the path forward, a welcome sight in the " \
         "otherwise choking darkness of the bog."

    p2 = "The heavy footfalls of your boots are silenced momentarily as one" \
         "of your legs sinks into a patch of mud, forcing you to wrest it " \
         "free. While brushing the muck off of your clothes, you're able " \
         "to get a good look at your surroundings. Everything as far as " \
         "the eye can see is buried beneath several feet of murky water, " \
         "including the path you've been taking up until this point, and " \
         "the fog shows no signs of thinning. You have no choice but to " \
         "continue forward."

    p3 = "While most of the path has been littered with ruined signage " \
         "whose inscriptions have long since faded, up ahead you're able " \
         "to spot what used to be an entire village. Houses and " \
         "storefronts alike sink into the gray-green murk and the mist " \
         "permeates the interiors of every building. Only gnats and " \
         "moss live here now."

    p4 = "You pause to rest after walking for what feels like an " \
         "eternity. Your pack hangs heavily on your shoulders and you " \
         "consider trying to light a campfire, but there hasn't been a " \
         "dry enough patch of land to accommodate a flame in miles. " \
         "Besides, as you stand in the middle of the bog, surrounded by " \
         "dark woods and the incessant buzzing of mosquitos, you feel as " \
         "if there is something just beyond the mist looking back at you."

    prompts = [p1, p2, p3, p4]
    return random.choice(prompts)


def get_flavor_line():
    end_string = ["You couldn't be any wetter.", "It's time to move on.",
                  "There's nothing left for you here.",
                  "Forward is the only way.",
                  "Just standing here gives you the creeps.",
                  "No rest for the wicked.",
                  "It would probably be best for you to go."]
    return random.choice(end_string)


def create_description_line(description, flavor_line):
    return "\n\n".join([textwrap.fill(description), flavor_line, ""])


def generate_room(num_foes=-1):
    """Randomly generates a room object to be explored by the player

    Keyword arguments:
    num_foes -- an optional number of enemies for the room

    Returns a room object."""
    random.seed()
    description = get_description()
    if num_foes == -1:
        num_foes = random.randint(0, 3)
    room = Room(description, num_foes)
    return room


def main():

    main_menu = Menu()
    main_menu.add_selection("Inventory")
    main_menu.add_selection("Explore")
    main_menu.add_selection("Status")

    # ip == "introductory prompt"
    ip = "You awaken in a dark thicket, choked by overgrowth and drowned" \
         "in swampwater. Mosquitos incessantly bite you through your" \
         "clothes and your boots are already waterlogged. The only source " \
         "of light comes from a torch twenty or so paces in the distance, " \
         "roaring strong with a flame that refuses to die in spite of the " \
         "rainwater dripping from the canopy above. Seeing no other " \
         "option, you bring yourself forward and grab ahold of it, " \
         "beginning your journey out of this blackened bog."
    print(create_description_line(ip, get_flavor_line()), main_menu, sep="")

    while (True):
        choice = input("> ")
        choice = choice.lower().strip()
        # TODO: check if num_enemies > 0
        # TODO: resolve_combat()
        if choice == "inventory":
            print("Placeholder loot bag")
        elif choice == "explore":
            room = generate_room()
            print(create_description_line(
                  room.description, get_flavor_line()), main_menu, sep="")
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

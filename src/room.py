import random
import textwrap
from .treasure import Treasure


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

    def get_treasure_object(self, treasure_name):
        """Get the first object associated with a given treasure

        Returns the first object in self._treasure with the
        same name as treasure_name and None if one could
        not be found."""

        for item in self._treasure:
            # Index 0 is the name and index 1 is the object reference
            if treasure_name == item[0]:
                return item[1]
        return None

    def get_treasure_printout(self):
        """Returns a formatted string of the entity's inventory"""
        printout = []

        # "Format: [number]x [item], [description]\n"
        # Ex. "1x Sword of Swording, It looks very sharp."
        for item in self._treasure:
            # Index 0 is the name of the treasure
            printout.append("".join(item[0]))
        return "\n".join(printout)

    def add_treasure(self, new_treasure):
        """Add the given treasure to the room

        Returns True if successful and False if the action failed
        due to the object to be added not being a Treasure"""
        if not isinstance(new_treasure, Treasure):
            return False
        self._treasure.append([new_treasure.name, new_treasure])
        return True

    def del_treasure(self, treasure):
        """Remove the given treasure from the room

        Returns True if successful and False if the action failed
        or if the object to be removed was not a Treasure."""
        if not isinstance(treasure, Treasure):
            return False
        if [treasure.name, treasure] not in self._treasure:
            return False
        self._treasure.remove([treasure.name, treasure])
        return True


def get_description():
    p1 = "As you trudge onwards, enduring the scrapes of brambled " \
         "overgrowth and pushing past the ruins of buildings lost to " \
         "time, you can feel a gentle rain coming from overhead. Just " \
         "above you, the thicket breaks just enough to let several wisps " \
         " of light illuminate the path forward, a welcome sight in the " \
         "otherwise choking darkness of the bog."

    p2 = "The heavy footfalls of your boots are stifled momentarily as one " \
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
    """Randomly selects a flavor line that follows a description."""
    end_string = ["You couldn't be any wetter.", "It's time to move on.",
                  "There's nothing left for you here.",
                  "Forward is the only way.",
                  "Just standing here gives you the creeps.",
                  "No rest for the wicked.",
                  "It would probably be best for you to go."]
    return random.choice(end_string)


def create_description_line(description, flavor_line):
    """Combines a description with a flavor line prettily."""
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

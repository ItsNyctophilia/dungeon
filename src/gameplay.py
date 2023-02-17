import random
from . import room
from .menu import Menu
from .monster import Monster
from .hero import Hero


def roll_dice(num_of_dice):
    """Roll the given amount of dice and save the results in a list"""
    random.seed()
    result = []
    # Randomly get a number between 1-6 for how many dice was given
    for x in range(num_of_dice):
        result.append(random.randint(1, 6))
    result.sort(reverse=True)
    return result


def roll_initiative():
    """Rolls 1 d6 dice for initiative."""
    # If the 1st roll is higher than the 2nd the player wins initiative
    if roll_dice(1) >= roll_dice(1):
        return True
    else:
        return False


def check_health(entity):
    """Checks if the entity has reached 0 HP."""
    if entity.hp == 0:
        return True
    else:
        return False


def check_hit(attacker, defender, flag):
    """Compares the attackers rolls to the defenders rolls"""
    attack = roll_dice(attacker.dice)
    defense = roll_dice(defender.dice)

    # If the flag was set print out the rolls
    if flag:
        print("Attacker:", attack)
        print("Defense:", defense)

    # Checks who has more Dice
    if len(attack) > len(defense):
        for x in range(len(defense)):
            if attack[x] > defense[x]:
                return True
            elif defense[x] > attack[x]:
                return False
            else:
                continue
        return True
    else:
        for x in range(len(attack)):
            if attack[x] > defense[x]:
                return True
            elif defense[x] > attack[x]:
                return False
            else:
                continue
        return False


def combat(player, monster, initiative, flag):
    """Loops through the combat until someone dies."""
    # TODO: End the program if the player dies
    while True:
        print("Your HP:", player.hp, "-", monster.name, "HP:", monster.hp)
        # If the initiative is true that means the player attacks first.
        if initiative:
            # Player attacks Monster
            if check_hit(player, monster, flag):
                print("Bonked the Monster!")
                monster.hit()
                if check_health(monster):
                    print("Monster died")
                    return True
            else:
                print("How did you miss?")

            # Monster attacks Player
            if check_hit(monster, player, flag):
                print("You took the hit like a Champ!")
                player.hit()
                if check_health(player):
                    return False
            else:
                print("The Monster might need some glasses!")
        else:
            # Monster attacks Player
            if check_hit(monster, player, flag):
                print("You took the hit like a Champ!")
                player.hit()
                if check_health(player):
                    return False
            else:
                print("The Monster might need some glasses!")

            # Player attacks Monster
            if check_hit(player, monster, flag):
                print("Bonked the Monster!")
                monster.hit()
                if check_health(monster):
                    print("Monster died")
                    return True
            else:
                print("How did you miss?")


def play_game(flag):
    """Function that plays Dungeon Dudes"""
    main_menu = Menu()
    main_menu.add_selection("Inventory")
    main_menu.add_selection("Explore")
    main_menu.add_selection("Status")
    main_menu.add_selection("Quit")

    player = Hero()

    # ip == "introductory prompt"
    ip = "You awaken in a dark thicket, choked by overgrowth and drowned " \
         "in swampwater. Mosquitos incessantly bite you through your " \
         "clothes and your boots are already waterlogged. The only source " \
         "of light comes from a torch twenty or so paces in the distance, " \
         "roaring strong with a flame that refuses to die in spite of the " \
         "rainwater dripping from the canopy above. Seeing no other " \
         "option, you bring yourself forward and grab ahold of it, " \
         "beginning your journey out of this blackened bog."
    print(room.create_description_line(ip, room.get_flavor_line()),
          main_menu, sep="")

    while (True):
        choice = input("> ")
        choice = choice.lower().strip()
        if choice == "inventory":

            print("Placeholder loot bag")

        elif choice == "explore":

            room_ = room.generate_room()
            print(room.create_description_line(
                  room_.description, room.get_flavor_line()))
            while room_.num_foes > 0:
                if not clear_room(player, room_, flag):
                    return False
            print(main_menu, sep="")

        elif choice == "status":

            print("Current Health:", player.hp)

        elif choice == "quit":

            print("Exiting....")
            return False

        else:

            print("Unrecognized command")


def clear_room(player, room_, flag):
    combat_menu = Menu()
    combat_menu.add_selection("Fight")
    combat_menu.add_selection("Investigate")
    combat_menu.add_selection("Inventory")
    combat_menu.add_selection("Status")
    combat_menu.add_selection("Quit")

    while (True):
        if room_.num_foes == 0:
            break

        print(combat_menu)
        choice = input("> ")
        choice = choice.lower().strip()

        if choice == "fight":
            monster = Monster.generate_monster()
            initiative = roll_initiative()
            if not combat(player, monster, initiative, flag):
                print("Game Over Dude!")
                return False
            room_.num_foes -= 1
            print("\n", room_.num_foes, " Monsters remaining!\n")

        elif choice == "inventory":

            print("Placeholder loot bag")

        elif choice == "investigate":

            print("Placeholder Investigate")

        elif choice == "status":

            print("Current Health:", player.hp)

        elif choice == "quit":

            print("Exiting....")
            return False

        else:

            print("Unrecognized command")

    return True

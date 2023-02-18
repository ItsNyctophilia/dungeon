import random
from . import treasure
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


def combat(player, monster, initiative, flag, buff=False):
    """Does 1 combat round"""
    # If the initiative is true that means the player attacks first.
    if buff:
        player.dice += 1

    if initiative:
        # Player attacks Monster
        if check_hit(player, monster, flag):
            print("Bonked the Monster!")
            monster.hit()
            if check_health(monster):
                print("Monster died")
                return 1
        else:
            print("How did you miss?")

        # Monster attacks Player
        if check_hit(monster, player, flag):
            print("You took the hit like a Champ!")
            player.hit()
            if check_health(player):
                return 0
        else:
            print("The Monster might need some glasses!")
    else:
        # Monster attacks Player
        if check_hit(monster, player, flag):
            print("You took the hit like a Champ!")
            player.hit()
            if check_health(player):
                return 0
        else:
            print("The Monster might need some glasses!")

        # Player attacks Monster
        if check_hit(player, monster, flag):
            print("Bonked the Monster!")
            monster.hit()
            if check_health(monster):
                print("Monster died")
                return 1
        else:
            print("How did you miss?")


def play_game(flag):
    """Function that plays Dungeon Dudes"""
    main_menu = Menu()
    main_menu.add_selection("Explore")
    main_menu.add_selection("Inventory")
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
    print(room.create_description_line(ip, room.get_flavor_line()))

    fight_flag = False

    while (True):
        print(main_menu, sep="")
        choice = input("> ")
        choice = choice.lower().strip()

        if (choice == "explore" or choice == "1") and not fight_flag:

            room_ = room.generate_room()

            print(room.create_description_line(
                  room_.description, room.get_flavor_line()))
            if room_.num_foes > 0:
                initiative = roll_initiative()
                main_menu.replace_selection("Fight", 0)
                fight_flag = True
        
        elif (choice == "fight" or choice == "1") and fight_flag :

            check = fight_monster(player, room_, initiative, flag)
            if check == 0:
                print("You died!")
                if not player.treasure:
                    print("Your bags were empty")
                else:
                    print("Inventory\n", player.get_treasure_printout())
                print("Exiting....")
                return False

            if not room_.treasure:
                shiny = False
                if main_menu.has_selection("Loot"):
                    main_menu.del_selection("Loot")
            else:
                shiny = True
                if not main_menu.has_selection("Loot"):
                    main_menu.add_selection("Loot")

            room_.num_foes -= 1

            print(room_.num_foes, "Monsters left!")
            if room_.num_foes == 0:
                main_menu.replace_selection("Explore", 0)
                fight_flag = False
        
        elif choice == "inventory" or choice == "2":

            if not player.treasure:
                print("Your bags are empty")
            else:
                print(player.get_treasure_printout())

        elif choice == "status" or choice == "3":

            print("Current Health:", player.hp)

        elif choice == "quit" or choice == "4":

            print("Exiting....")
            return False

        elif (choice == "loot" or choice == "5") and shiny:
            print(room_.get_treasure_printout())
            while True:
                item = input("Type the name of the item to loot or back: ")
                treasure_ = room_.get_treasure_object(item)
                if item == "back":
                    break
                elif treasure_ is None:
                    print("Invalid item name!")
                    continue
                else:
                    player.add_treasure(treasure_)
                    room_.del_treasure(treasure_)
                    if not room_.treasure:
                        if main_menu.has_selection("Loot"):
                            main_menu.del_selection("Loot")
                    print(f'{treasure_.name} picked up!')
                    break

        else:

            print("Unrecognized command")


def fight_monster(player, room_, initiative, flag):
    combat_menu = Menu()
    combat_menu.add_selection("Attack")
    combat_menu.add_selection("Investigate")
    combat_menu.add_selection("Inventory")
    combat_menu.add_selection("Status")

    monster = Monster.generate_monster()

    if random.randint(0, 100) < (monster.hp + monster.dice) * 10:
        room_.add_treasure(treasure.get_treasure())

    buff = False

    print(monster.description)
    while (True):
        print("\nYour HP:", player.hp, "-", monster.name.strip("\""), "HP:",
              monster.hp)
        print(combat_menu)
        choice = input("> ")
        choice = choice.lower().strip()

        if choice == "attack" or choice == "1":

            check = combat(player, monster, initiative, flag, buff)

            if buff:
                player.dice -= 1
                buff = False

            if check == 1 or check == 0:
                return check

        elif choice == "investigate" or choice == "2":

            print("Monster Health:", monster.hp)

        elif choice == "inventory" or choice == "3":

            if not player.treasure:
                print("Your bags are empty")
            else:
                print(player.get_treasure_printout())
                if player.has_treasure("Attack Potion"):
                    potion = input("Want to use a potion? Yes/No: ")
                    while True:
                        potion = potion.lower().strip()
                        if potion == "yes":
                            print("Plus 1 dice on your next attack!")
                            buff = True
                            break
                        elif potion == "no":
                            break
                        else:
                            print("Invalid Input")
                            potion = input("Yes/No: ")
                            continue

        elif choice == "status" or choice == "4":

            print("Current Health:", player.hp)

        else:

            print("Unrecognized command")

#!/usr/bin/env python3


from optparse import OptionParser
import src.room as room
import src.gameplay as game
from src.menu import Menu
from src.monster import Monster
from src.hero import Hero


def main():

    parser = OptionParser()
    parser.add_option("-d", "--dice", help="Print dice rolls to the screen.",
                      action='store_true', default=False, dest='flag')
    options = parser.parse_args

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
                  room_.description, room.get_flavor_line()),
                  main_menu, sep="")
            if room_.num_foes > 0:
                if not main_menu.has_selection("Fight"):
                    main_menu.add_selection("Fight")
            else:
                if main_menu.has_selection("Fight"):
                    main_menu.del_selection("Fight")
            continue

        elif choice == "status":

            print("Current Health:", player.hp)

        elif choice == "quit":

            print("Exiting....")
            exit()

        elif choice == "fight":
            monster = Monster.generate_monster()
            initiative = game.roll_initiative()
            game.combat(player, monster, initiative, options)
            print(main_menu)

        else:

            print("Unrecognized command")


if __name__ == "__main__":
    try:
        main()
    except (Exception, GeneratorExit, KeyboardInterrupt, SystemExit) as e:
        name = type(e).__name__
        print("Exception of type", name, "prevented program from continuing!")

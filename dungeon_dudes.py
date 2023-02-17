#!/usr/bin/env python3


from optparse import OptionParser
import src.gameplay as game


def main():

    parser = OptionParser()
    parser.add_option("-d", "--dice", help="Print dice rolls to the screen.",
                      action='store_true', default=False, dest='flag')
    (options, args) = parser.parse_args()

    game.play_game(options.flag)


if __name__ == "__main__":
    try:
        main()
    except (Exception, GeneratorExit, KeyboardInterrupt, SystemExit) as e:
        name = type(e).__name__
        print("Exception of type", name, "prevented program from continuing!")

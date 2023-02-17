import random


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
                    break
            else:
                print("How did you miss?")

            # Monster attacks Player
            if check_hit(monster, player, flag):
                print("You took the hit like a Champ!")
                player.hit()
                if check_health(player):
                    print("Game Over Loser!")
                    break
            else:
                print("The Monster might need some glasses!")
        else:
            # Monster attacks Player
            if check_hit(monster, player, flag):
                print("You took the hit like a Champ!")
                player.hit()
                if check_health(player):
                    print("Game Over Loser!")
                    break
            else:
                print("The Monster might need some glasses!")

            # Player attacks Monster
            if check_hit(player, monster, flag):
                print("Bonked the Monster!")
                monster.hit()
                if check_health(monster):
                    print("Monster died")
                    break
            else:
                print("How did you miss?")

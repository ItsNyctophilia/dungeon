import random


def roll_dice(num_of_dice):
    """Roll the given amount of dice and save the results in a list"""
    random.seed()
    result = []
    for x in range(num_of_dice):
        result.append(random.randint(1, 6))
    result.sort(reverse=True)
    return result


def roll_initiative():
    """Rolls 1 d6 dice for initiative."""
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

    if flag:
        print("Attacker:", attack)
        print("Defense:", defense)

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

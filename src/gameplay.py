import random


def roll_dice(num_of_dice):
    """Roll the given amount of dice and save the results in a list"""
    random.seed()
    result = []
    for x in range(num_of_dice):
        result.append(random.randint(1, 6))
    result.sort(reverse=True)
    return result

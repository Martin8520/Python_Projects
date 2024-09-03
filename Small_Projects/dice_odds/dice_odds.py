import itertools
from collections import Counter


def average_roll(num_dice):
    """
    Calculate the average roll of a given number of D6 dice.
    """
    return num_dice * 3.5


def roll_probabilities(num_dice):
    """
    Calculate the percentage chance of all possible roll outcomes with a given number of D6 dice.
    """
    possible_rolls = range(1, 7)
    all_combinations = itertools.product(possible_rolls, repeat=num_dice)

    roll_sums = [sum(combination) for combination in all_combinations]
    roll_counts = Counter(roll_sums)

    total_combinations = 6 ** num_dice
    probabilities = {roll_total: (count / total_combinations) * 100
                     for roll_total, count in roll_counts.items()}

    return probabilities


def specific_roll_probability(num_dice, target_sum):
    """
    Calculate the percentage chance of rolling a specific total with a given number of D6 dice.
    """
    probabilities = roll_probabilities(num_dice)
    return probabilities.get(target_sum, 0)


if __name__ == "__main__":
    num_dice = 3
    target_sum = 10

    avg_roll = average_roll(num_dice)
    print(f"Average roll with {num_dice} D6 dice: {avg_roll}")

    probabilities = roll_probabilities(num_dice)
    print(f"Probabilities for all possible rolls with {num_dice} D6 dice:")
    for roll_total, probability in sorted(probabilities.items()):
        print(f"Total {roll_total}: {probability:.2f}%")

    specific_prob = specific_roll_probability(num_dice, target_sum)
    print(f"Probability of rolling a total of {target_sum} with {num_dice} D6 dice: {specific_prob:.2f}%")

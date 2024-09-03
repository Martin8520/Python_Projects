import math
from scipy.stats import norm


def average_roll(num_dice):
    return num_dice * 3.5


def standard_deviation(num_dice):
    return math.sqrt(num_dice * 35 / 12)


def specific_roll_probability_approx(num_dice, target_sum):
    mean = average_roll(num_dice)
    stddev = standard_deviation(num_dice)

    cumulative_prob = norm.cdf(target_sum + 0.5, mean, stddev) - norm.cdf(target_sum - 0.5, mean, stddev)
    return cumulative_prob * 100


if __name__ == "__main__":
    num_dice = int(input("Enter the number of D6 dice: "))
    target_sum = int(input("Enter the roll total you're looking to get: "))

    avg_roll = average_roll(num_dice)
    print(f"\nAverage roll with {num_dice} D6 dice: {avg_roll:.2f}")

    specific_prob = specific_roll_probability_approx(num_dice, target_sum)
    print(f"Probability of rolling a total of {target_sum} with {num_dice} D6 dice: {specific_prob:.6f}%")

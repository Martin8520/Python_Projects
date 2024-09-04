import tkinter as tk
from tkinter import messagebox
import itertools
from collections import Counter
import math
from scipy.stats import norm
from math import comb


def average_roll(num_dice):
    return num_dice * 3.5


def standard_deviation(num_dice):
    return math.sqrt(num_dice * 35 / 12)


def roll_probabilities(num_dice):
    possible_rolls = range(1, 7)
    all_combinations = itertools.product(possible_rolls, repeat=num_dice)

    roll_sums = [sum(combination) for combination in all_combinations]
    roll_counts = Counter(roll_sums)

    total_combinations = 6 ** num_dice
    probabilities = {roll_total: (count / total_combinations) * 100
                     for roll_total, count in roll_counts.items()}

    return probabilities


def specific_roll_probability_exact(num_dice, target_sum):
    probabilities = roll_probabilities(num_dice)
    return probabilities.get(target_sum, 0)


def probability_for_or_higher_exact(num_dice, target_sum):
    probabilities = roll_probabilities(num_dice)
    cumulative_prob = sum(prob for roll, prob in probabilities.items() if roll >= target_sum)
    return cumulative_prob


def specific_roll_probability_approx(num_dice, target_sum):
    mean = average_roll(num_dice)
    stddev = standard_deviation(num_dice)

    cumulative_prob = norm.cdf(target_sum + 0.5, mean, stddev) - norm.cdf(target_sum - 0.5, mean, stddev)
    return cumulative_prob * 100


def probability_for_or_higher_approx(num_dice, target_sum):
    mean = average_roll(num_dice)
    stddev = standard_deviation(num_dice)

    cumulative_prob = norm.sf(target_sum - 0.5, mean, stddev)
    return cumulative_prob * 100


def calculate_same_roll_probability(num_dice, target_face, num_faces):
    p_single = 1 / 6
    p_other = 1 - p_single

    probability = comb(num_dice, num_faces) * (p_single ** num_faces) * (p_other ** (num_dice - num_faces))
    return probability * 100


def calculate():
    try:
        num_dice = int(entry_num_dice.get())
        target_input = entry_target_sum.get()

        if num_dice <= 0:
            messagebox.showerror("Input Error", "Number of dice must be greater than 0.")
            return

        use_exact = num_dice <= 10

        if target_input.endswith("+"):
            target_sum = int(target_input[:-1])
            specific_prob = (probability_for_or_higher_exact(num_dice, target_sum) if use_exact
                             else probability_for_or_higher_approx(num_dice, target_sum))
            label_probability_result.config(text=f"Probability of {target_sum}+ Roll: {specific_prob:.6f}%")
        else:
            target_sum = int(target_input)
            specific_prob = (specific_roll_probability_exact(num_dice, target_sum) if use_exact
                             else specific_roll_probability_approx(num_dice, target_sum))
            label_probability_result.config(text=f"Probability of Rolling {target_sum}: {specific_prob:.6f}%")

        avg_roll = average_roll(num_dice)
        label_average_result.config(text=f"Average Roll: {avg_roll:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for the number of dice and target roll total.")


def calculate_same_roll():
    try:
        num_dice = int(entry_num_dice_same.get())
        target_face = int(entry_target_face.get())
        num_faces = int(entry_num_faces.get())

        if num_dice <= 0 or num_faces > num_dice or target_face < 1 or target_face > 6:
            messagebox.showerror("Input Error", "Please enter valid numbers for the dice, faces, and occurrences.")
            return

        same_roll_prob = calculate_same_roll_probability(num_dice, target_face, num_faces)
        label_same_roll_result.config(text=f"Probability of Rolling {num_faces} x {target_face}: {same_roll_prob:.6f}%")

    except ValueError:
        messagebox.showerror("Input Error",
                             "Please enter valid integers for the number of dice, target face, and number of faces.")


root = tk.Tk()
root.title("Dice Roll Probability Calculator")

root.geometry("400x550")

label_num_dice = tk.Label(root, text="Number of D6 Dice:")
label_num_dice.pack(pady=5)
entry_num_dice = tk.Entry(root)
entry_num_dice.pack(pady=5)

label_target_sum = tk.Label(root, text="Target Roll Total (e.g., 3 or 3+):")
label_target_sum.pack(pady=5)
entry_target_sum = tk.Entry(root)
entry_target_sum.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

label_average_result = tk.Label(root, text="Average Roll: ")
label_average_result.pack(pady=5)
label_probability_result = tk.Label(root, text="Probability: ")
label_probability_result.pack(pady=5)

separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=10)

label_num_dice_same = tk.Label(root, text="Number of D6 Dice for Specific Faces:")
label_num_dice_same.pack(pady=5)
entry_num_dice_same = tk.Entry(root)
entry_num_dice_same.pack(pady=5)

label_target_face = tk.Label(root, text="Specific Face Value (1-6):")
label_target_face.pack(pady=5)
entry_target_face = tk.Entry(root)
entry_target_face.pack(pady=5)

label_num_faces = tk.Label(root, text="Number of Times This Face Should Appear:")
label_num_faces.pack(pady=5)
entry_num_faces = tk.Entry(root)
entry_num_faces.pack(pady=5)

button_same_roll = tk.Button(root, text="Calculate Same Roll Probability", command=calculate_same_roll)
button_same_roll.pack(pady=10)

label_same_roll_result = tk.Label(root, text="Probability of Rolling Same Faces: ")
label_same_roll_result.pack(pady=5)

root.mainloop()

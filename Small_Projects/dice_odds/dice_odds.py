import tkinter as tk
from tkinter import messagebox
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


def calculate():
    try:
        num_dice = int(entry_num_dice.get())
        target_sum = int(entry_target_sum.get())

        if num_dice <= 0:
            messagebox.showerror("Input Error", "Number of dice must be greater than 0.")
            return

        avg_roll = average_roll(num_dice)
        specific_prob = specific_roll_probability_approx(num_dice, target_sum)

        label_average_result.config(text=f"Average Roll: {avg_roll:.2f}")
        label_probability_result.config(text=f"Probability: {specific_prob:.6f}%")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for the number of dice and target roll total.")


root = tk.Tk()
root.title("Dice Roll Probability Calculator")

label_num_dice = tk.Label(root, text="Number of D6 Dice:")
label_num_dice.pack(pady=5)
entry_num_dice = tk.Entry(root)
entry_num_dice.pack(pady=5)

label_target_sum = tk.Label(root, text="Target Roll Total:")
label_target_sum.pack(pady=5)
entry_target_sum = tk.Entry(root)
entry_target_sum.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

label_average_result = tk.Label(root, text="Average Roll: ")
label_average_result.pack(pady=5)
label_probability_result = tk.Label(root, text="Probability: ")
label_probability_result.pack(pady=5)

root.mainloop()

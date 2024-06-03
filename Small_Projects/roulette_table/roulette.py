import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("American Roulette")

roulette_numbers = [str(i) for i in range(1, 37)] + ['0', '00']
number_colors = {str(i): "red" if i % 2 != 0 else "black" for i in range(1, 11)}
number_colors.update({str(i): "black" if i % 2 != 0 else "red" for i in range(11, 19)})
number_colors.update({str(i): "red" if i % 2 != 0 else "black" for i in range(19, 29)})
number_colors.update({str(i): "black" if i % 2 != 0 else "red" for i in range(29, 37)})
number_colors['0'] = "green"
number_colors['00'] = "green"


def spin():
    result = random.choice(roulette_numbers)
    color = number_colors[result]
    messagebox.showinfo("Roulette Result", f"The ball landed on {result} ({color})")


buttons = []
for number in roulette_numbers:
    text_color = "white" if number_colors[number] == "black" else "black"
    btn = tk.Button(root, text=number, width=5, height=2, bg=number_colors[number], fg=text_color, command=spin)
    buttons.append(btn)

for i, btn in enumerate(buttons):
    row = i // 4
    col = i % 4
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

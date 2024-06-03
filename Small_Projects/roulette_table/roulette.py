import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("American Roulette")

# Define the roulette numbers including 0 and 00
roulette_numbers = [str(i) for i in range(1, 37)] + ['0', '00']

# Create a dictionary for colors
number_colors = {str(i): "red" if i % 2 != 0 else "black" for i in range(1, 37)}
number_colors['0'] = "green"
number_colors['00'] = "green"

# Function to spin the roulette and display the result
def spin():
    result = random.choice(roulette_numbers)
    color = number_colors[result]
    messagebox.showinfo("Roulette Result", f"The ball landed on {result} ({color})")

# Function to handle black/red bet
def black_red_bet(choice):
    result = random.choice(roulette_numbers)
    color = number_colors[result]
    if (choice == "Black" and color == "black") or (choice == "Red" and color == "red"):
        messagebox.showinfo("Bet Result", f"Congratulations! You won. The ball landed on {result} ({color})")
    else:
        messagebox.showinfo("Bet Result", f"Sorry! You lost. The ball landed on {result} ({color})")

# Function to handle thirds bet
def thirds_bet(choice):
    result = random.choice(roulette_numbers)
    if choice == "1st Third" and result in [str(i) for i in range(1, 13)]:
        messagebox.showinfo("Bet Result", f"Congratulations! You won. The ball landed on {result}")
    elif choice == "2nd Third" and result in [str(i) for i in range(13, 25)]:
        messagebox.showinfo("Bet Result", f"Congratulations! You won. The ball landed on {result}")
    elif choice == "3rd Third" and result in [str(i) for i in range(25, 37)]:
        messagebox.showinfo("Bet Result", f"Congratulations! You won. The ball landed on {result}")
    else:
        messagebox.showinfo("Bet Result", f"Sorry! You lost. The ball landed on {result}")

# Function to handle odds/evens bet
def odds_evens_bet(choice):
    result = random.choice(roulette_numbers)
    if (choice == "Odds" and result != '0' and result != '00' and int(result) % 2 != 0) or \
            (choice == "Evens" and result != '0' and result != '00' and int(result) % 2 == 0):
        messagebox.showinfo("Bet Result", f"Congratulations! You won. The ball landed on {result}")
    else:
        messagebox.showinfo("Bet Result", f"Sorry! You lost. The ball landed on {result}")

# Create buttons for different betting options
black_btn = tk.Button(root, text="Black", width=10, height=2, bg="black", fg="white", command=lambda: black_red_bet("Black"))
black_btn.grid(row=0, column=0, padx=5, pady=5)

red_btn = tk.Button(root, text="Red", width=10, height=2, bg="red", command=lambda: black_red_bet("Red"))
red_btn.grid(row=0, column=1, padx=5, pady=5)

first_third_btn = tk.Button(root, text="1st Third", width=10, height=2, bg="green", command=lambda: thirds_bet("1st Third"))
first_third_btn.grid(row=1, column=0, padx=5, pady=5)

second_third_btn = tk.Button(root, text="2nd Third", width=10, height=2, bg="green", command=lambda: thirds_bet("2nd Third"))
second_third_btn.grid(row=1, column=1, padx=5, pady=5)

third_third_btn = tk.Button(root, text="3rd Third", width=10, height=2, bg="green", command=lambda: thirds_bet("3rd Third"))
third_third_btn.grid(row=1, column=2, padx=5, pady=5)

odds_btn = tk.Button(root, text="Odds", width=10, height=2, bg="blue", fg="white", command=lambda: odds_evens_bet("Odds"))
odds_btn.grid(row=2, column=0, padx=5, pady=5)

evens_btn = tk.Button(root, text="Evens", width=10, height=2, bg="yellow", command=lambda: odds_evens_bet("Evens"))
evens_btn.grid(row=2, column=1, padx=5, pady=5)

spin_btn = tk.Button(root, text="Spin", width=10, height=2, bg="gray", command=spin)
spin_btn.grid(row=2, column=2, padx=5, pady=5)

# Create labels for the numbers
for i, number in enumerate(roulette_numbers):
    color = number_colors[number]
    label = tk.Label(root, text=number, bg=color, fg="white" if color == "black" else "black", width=5, height=2)
    label.grid(row=i//4+3, column=i%4, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()

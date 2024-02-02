import random

sides = [4, 6, 8, 10, 12, 20, 100]

while True:
    num_dice = int(input("How many dice would you like to roll? "))
    num_sides = int(input("How many sides does the die have? "))

    if num_sides not in sides:
        print("Sorry, that is not a valid die type. Choose from 4, 6, 8, 10, 12, or 20.")
    else:
        break

total_score = 0
for i in range(num_dice):
    roll = random.randint(1, num_sides)
    total_score += roll
    print(f"You rolled a {roll} on a {num_sides}-sided die.")

    if num_sides == 20 and roll == 20:
        print("20!")
    else:
        continue

print(f"Total score: {total_score}")

names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

roulette = random.randint(0, len(names) - 1)

selected_person = names[roulette]

print(f"{selected_person} is going to buy the meal today!")
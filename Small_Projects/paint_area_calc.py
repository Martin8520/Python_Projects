# Write your code below this line 👇
from math import ceil


def paint_calc(height, width, cover):
    can_num = (height * width) / cover
    print(f"You'll need {ceil(can_num)} cans of paint")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

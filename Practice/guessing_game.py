import random

random_num = random.randint(1, 10)

user_num = int(input("Guess a number from 1 to 10: "))

if user_num > 10 or user_num < 1:
    print("The number you picked is outside the range of 1 to 10")
elif user_num == random_num:
    print(f"You guessed the number {random_num} correctly!")
elif user_num != random_num:
    print(f"You guessed {user_num}, but the correct number was {random_num}")


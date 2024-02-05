import random

run = True
print(f"I'm thinking of a number between 1 and 100")
random_num = random.randint(1, 100)
lives = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")

if difficulty == "easy":
    lives += 10
    print(f"You have {lives} attempts remaining to guess the number")
elif difficulty == "hard":
    lives += 5
    print(f"You have {lives} attempts remaining to guess the number")

while run is True:
    guess = int(input("Make a guess: "))

    if guess > random_num:
        print("Too high.")
        lives -= 1
        if lives == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again")
            print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print("Too low.")
        lives -= 1
        if lives == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again")
            print(f"You have {lives} attempts remaining to guess the number.")

    if guess == random_num:
        print(f"You got it! The answer was {random_num}")
        run = False
    elif lives == 0:
        run = False
    else:
        run = True

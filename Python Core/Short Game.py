import time

def delay_print(text, delay=0.2):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_over():
    delay_print("Game Over! Do you want to play again? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        start_game()
    else:
        delay_print("Thanks for playing! Goodbye!")

def start_game():
    delay_print("Welcome to your first Adventure!")
    delay_print("You find yourself standing at a crossroad.")
    delay_print("To the left is a dark forest.")
    delay_print("To the right is a sunny beach.")
    delay_print("Which path do you choose? (left/right)")

    choice1 = input().lower()

    if choice1 == "left":
        delay_print("You enter the dark forest and encounter a mysterious creature.")
        delay_print("It offers you a magical amulet. Do you take it? (yes/no)")

        choice2 = input().lower()

        if choice2 == "yes":
            delay_print("The amulet grants you the power to communicate with animals.")
            delay_print("You continue your journey and befriend a wise owl.")
            delay_print("Congratulations! You have a new friend and a magical amulet.")
        else:
            delay_print("You decide not to take the amulet.")
            delay_print("You exit the forest and return to the crossroad.")
            game_over()
    elif choice1 == "right":
        delay_print("You head to the sunny beach and discover a treasure chest buried in the sand.")
        delay_print("Do you open it? (yes/no)")

        choice3 = input().lower()

        if choice3 == "yes":
            delay_print("You open the chest and find it filled with gold coins and jewels!")
            delay_print("Congratulations! You're now a wealthy adventurer.")
        else:
            delay_print("You decide not to open the chest.")
            delay_print("You leave the beach and return to the crossroad.")
            game_over()
    else:
        delay_print("Invalid choice. Please enter 'left' or 'right'.")
        start_game()

start_game()
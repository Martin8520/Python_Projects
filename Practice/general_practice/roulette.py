import random


def spin_wheel():
    return random.randint(0, 36)


def check_result(number, bet):
    if bet == "Even" and number % 2 == 0:
        return True
    elif bet == "Odd" and number % 2 != 0:
        return True
    elif bet.isdigit() and int(bet) == number:
        return True
    elif bet.lower() == "red" and number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return True
    elif bet.lower() == "black" and number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        return True
    else:
        return False


def roulette_game():
    print("Welcome to Roulette!")
    while True:
        print("\nPlace your bet:")
        print("1. Even")
        print("2. Odd")
        print("3. Red")
        print("4. Black")
        print("5. Single Number (0 to 36)")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thanks for playing!")
            break

        if choice == "5":
            number_bet = input("Enter the number you want to bet on (0 to 36): ")
            if not number_bet.isdigit() or int(number_bet) < 0 or int(number_bet) > 36:
                print("Invalid input! Please enter a number between 0 and 36.")
                continue
            bet_amount = int(input("Enter your bet amount: "))
        else:
            bet_amount = int(input("Enter your bet amount: "))

        wheel_result = spin_wheel()
        print("The wheel spins... It lands on", wheel_result)

        if choice in ["1", "2", "3", "4"]:
            bet_types = ["Even", "Odd", "Red", "Black"]
            bet = bet_types[int(choice) - 1]
        else:
            bet = number_bet

        if check_result(wheel_result, bet):
            print("Congratulations! You win", bet_amount * 2, "coins!")
        else:
            print("Sorry, you lose.")


roulette_game()

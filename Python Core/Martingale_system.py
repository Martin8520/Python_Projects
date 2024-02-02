def show_info():
    print(
        "The Martingale system is a betting strategy where each time you lose, you need to double your "
        "previous bet until\n"
        "you win, and then the process starts over again.\n"
        "This program calculates how many times in a row you can afford\n"
        "to lose and what are the odds of losing that many times.\n"
        "On the first input line, type a positive integer that represents your total sum of money.\n"
        "On the second input line, type a positive integer that represents your initial bet.\n"
        "On the third input line, type a positive float that represents your win/lose ratio.\n"
        "Here are some examples for win/lose ratios you can use:\n"
        "0.5 is the equivalent of a coin flip or 50/50 odds.\n"
        "0.513514 is the equivalent of hitting red/black in European roulette with one green.\n"
        "0.526316 is the equivalent of hitting red/black in American roulette with two greens.\n"
        "0.972973 is the equivalent of hitting green in European roulette with one green\n"
        "0.947368 is the equivalent of hitting green in American roulette with two greens\n"
        "A ratio of 1.0 or higher will always result in a 100% loss.")


info = False

if not info:
    info_input = input("Would you like to read the info? (y/n): ").lower()
    if info_input == "y":
        show_info()
        info = True
    elif info_input == "n":
        pass
    else:
        print("Invalid input.")

while True:
    try:
        total_cash = int(input("Enter your current cash: "))
        initial_bet = int(input("Enter your initial bet: "))
        chance_to_lose = float(input("Input your win ratio: "))

        if total_cash <= 0 or initial_bet <= 0 or chance_to_lose <= 0 or chance_to_lose >= 1 or initial_bet >= total_cash:
            print("Enter only positive integers. Your win/lose ratio should also be less than 1. Your initial bet "
                  "should also be less than your total cash")
            continue

        total_bets = 1
        total_cash -= initial_bet
        print(f"After losing your initial bet of ${initial_bet}, you have ${total_cash} left.")

        while total_cash >= initial_bet * 2:
            bet_amount = initial_bet * 2

            total_bets += 1
            total_cash -= bet_amount
            print(f"${total_cash} left after {total_bets} losses with a bet amount of ${bet_amount}.")

            initial_bet = bet_amount

        if total_bets >= 0:
            print(f"You can afford to lose a total of {total_bets} times in a row.")
            percent_chance = (chance_to_lose ** total_bets) * 100
            odds = ((percent_chance / 100) / 1) * 1000
            print(f"{percent_chance:.2f}% chance of losing {total_bets} times in a row, or odds of {odds:.0f} in 1000 ")

        while True:
            again = input("Run again, exit or see the info? (run/exit/info): ").lower()

            if again in ("run", "exit", "info"):
                break
            print("Invalid input.")

        if again == "info":
            info = False
            show_info()
            continue

        if again == "exit":
            break

    except ValueError:
        print("Invalid input. Please use only positive integers for your current cash and initial bet, and use only "
              "positive floats for your win/loss ratio")

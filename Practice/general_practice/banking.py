account_name = input("Enter your first and last name: ").title().split(" ")
account_money = 0
banking = True
while banking is True:
    print("Type 'deposit' to deposit money into your account\n"
          "Type 'withdraw' to withdraw money from your account\n"
          "Type 'balance' to check your account balance")
    command = input("What would you like to do?: ")
    if command == "deposit":
        deposit = float(input("How much money would you like to deposit?: $").lower())
        account_money += deposit
        print(f"Your current balance is {account_money:.2f}")
    elif command == "withdraw":
        withdraw = float(input("How much money would you like to withdraw?: $").lower())
        if withdraw > account_money:
            print("Insufficient balance in your account")
            print(f"Your current balance is {account_money:.2f}")
        else:
            account_money -= withdraw
            print(f"Your current balance is {account_money:.2f}")
    elif command == "balance":
        print(f"Your current balance is {account_money:.2f}")

    exit_program = input("Type 'exit' if you want to exit the program.\n"
                         "Type 'continue' if you want to continue the program.").lower()
    if exit_program == "exit":
        banking = False
    elif exit_program == "continue":
        banking = True
    else:
        print("Invalid input")

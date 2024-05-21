import os

FILE_NAME = "transactions.txt"


def load_transactions():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        transactions = file.readlines()
    return [line.strip().split(",") for line in transactions]


def save_transactions(transactions):
    with open(FILE_NAME, "w") as file:
        for transaction in transactions:
            file.write(",".join(transaction) + "\n")


def add_transaction(transactions):
    t_type = input("Enter transaction type (income/expense): ").strip()
    amount = input("Enter amount: ").strip()
    description = input("Enter description: ").strip()
    transactions.append([t_type, amount, description])
    save_transactions(transactions)
    print("Transaction added!")


def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return
    for i, transaction in enumerate(transactions, 1):
        print(f"{i}. {transaction[0]}, {transaction[1]}, {transaction[2]}")


def delete_transaction(transactions):
    view_transactions(transactions)
    try:
        index = int(input("Enter the number of the transaction to delete: "))
        if 1 <= index <= len(transactions):
            transactions.pop(index - 1)
            save_transactions(transactions)
            print("Transaction deleted!")
        else:
            print("Invalid transaction number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def view_balance(transactions):
    balance = 0
    for t_type, amount, _ in transactions:
        if t_type == "income":
            balance += float(amount)
        elif t_type == "expense":
            balance -= float(amount)
    print(f"Current balance: {balance}")


def main():
    transactions = load_transactions()
    while True:
        print("\nWelcome to Personal Finance Tracker!")
        print("What would you like to do?")
        print("1. Add a transaction")
        print("2. View transactions")
        print("3. Delete a transaction")
        print("4. View balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            delete_transaction(transactions)
        elif choice == "4":
            view_balance(transactions)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

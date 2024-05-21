import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

FILE_NAME = "transactions.csv"


def load_transactions(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r", newline='') as file:
        reader = csv.reader(file)
        return list(reader)


def save_transactions(file_name, transactions):
    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transactions)


def add_transaction(transactions, tree):
    t_type = simpledialog.askstring("Transaction Type", "Enter transaction type (income/expense):").strip()
    amount = simpledialog.askstring("Amount", "Enter amount:").strip()
    description = simpledialog.askstring("Description", "Enter description:").strip()
    transactions.append([t_type, amount, description])
    save_transactions(FILE_NAME, transactions)
    update_treeview(tree, transactions)
    messagebox.showinfo("Success", "Transaction added!")


def view_transactions(transactions, tree):
    update_treeview(tree, transactions)


def delete_transaction(transactions, tree):
    selected_item = tree.selection()[0]
    transaction_index = int(tree.item(selected_item)['text']) - 1
    transactions.pop(transaction_index)
    save_transactions(FILE_NAME, transactions)
    update_treeview(tree, transactions)
    messagebox.showinfo("Success", "Transaction deleted!")


def view_balance(transactions):
    balance = 0
    for t_type, amount, _ in transactions:
        if t_type == "income":
            balance += float(amount)
        elif t_type == "expense":
            balance -= float(amount)
    messagebox.showinfo("Balance", f"Current balance: {balance}")


def update_treeview(tree, transactions):
    for item in tree.get_children():
        tree.delete(item)
    for i, transaction in enumerate(transactions, 1):
        tree.insert('', 'end', text=i, values=transaction)


def open_file(tree):
    global FILE_NAME
    file_name = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_name:
        FILE_NAME = file_name
        transactions = load_transactions(FILE_NAME)
        update_treeview(tree, transactions)


def create_new_file(tree):
    global FILE_NAME
    file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_name:
        FILE_NAME = file_name
        transactions = []
        save_transactions(FILE_NAME, transactions)
        update_treeview(tree, transactions)


def main():
    root = tk.Tk()
    root.title("Personal Finance Tracker")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    tree = ttk.Treeview(frame, columns=('Type', 'Amount', 'Description'))
    tree.heading('#0', text='Index')
    tree.heading('#1', text='Type')
    tree.heading('#2', text='Amount')
    tree.heading('#3', text='Description')
    tree.column('#0', width=50)
    tree.column('#1', width=100)
    tree.column('#2', width=100)
    tree.column('#3', width=200)
    tree.grid(row=0, column=0, columnspan=4)

    add_button = ttk.Button(frame, text="Add Transaction", command=lambda: add_transaction(transactions, tree))
    add_button.grid(row=1, column=0, pady=5)

    view_button = ttk.Button(frame, text="View Transactions", command=lambda: view_transactions(transactions, tree))
    view_button.grid(row=1, column=1, pady=5)

    delete_button = ttk.Button(frame, text="Delete Transaction", command=lambda: delete_transaction(transactions, tree))
    delete_button.grid(row=1, column=2, pady=5)

    balance_button = ttk.Button(frame, text="View Balance", command=lambda: view_balance(transactions))
    balance_button.grid(row=1, column=3, pady=5)

    open_button = ttk.Button(frame, text="Open File", command=lambda: open_file(tree))
    open_button.grid(row=2, column=0, pady=5)

    new_button = ttk.Button(frame, text="New File", command=lambda: create_new_file(tree))
    new_button.grid(row=2, column=1, pady=5)

    global transactions
    transactions = load_transactions(FILE_NAME)
    update_treeview(tree, transactions)

    root.mainloop()


if __name__ == "__main__":
    main()

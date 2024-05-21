import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

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


def prompt_transaction_type():
    dialog = tk.Toplevel()
    dialog.title("Select Transaction Type")
    tk.Label(dialog, text="Choose transaction type:").pack(pady=10)
    type_var = tk.StringVar()

    def set_type(t_type):
        type_var.set(t_type)
        dialog.destroy()

    tk.Button(dialog, text="Income", command=lambda: set_type("income")).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(dialog, text="Expense", command=lambda: set_type("expense")).pack(side=tk.RIGHT, padx=10, pady=10)

    dialog.wait_window()
    return type_var.get()


def prompt_transaction_details():
    dialog = tk.Toplevel()
    dialog.title("Enter Transaction Details")

    tk.Label(dialog, text="Amount:").pack(pady=5, padx=5)
    amount_entry = tk.Entry(dialog)
    amount_entry.pack(pady=5)

    tk.Label(dialog, text="Description:").pack(pady=5, padx=5)
    description_entry = tk.Entry(dialog)
    description_entry.pack(pady=5, padx=5)

    details = {}

    def submit():
        details['amount'] = amount_entry.get()
        details['description'] = description_entry.get()
        dialog.destroy()

    tk.Button(dialog, text="Submit", command=submit).pack(pady=10)

    dialog.wait_window()
    return details


def add_transaction(tree, balance_label):
    global transactions
    t_type = prompt_transaction_type()
    if not t_type:
        return

    details = prompt_transaction_details()
    if not details['amount'] or not details['description']:
        messagebox.showerror("Error", "All fields are required!")
        return

    transactions.append([t_type, details['amount'], details['description']])
    save_transactions(FILE_NAME, transactions)
    update_treeview(tree, transactions)
    update_balance(balance_label)


def view_transactions(tree):
    global transactions
    update_treeview(tree, transactions)


def delete_transaction(tree, balance_label):
    global transactions
    selected_item = tree.selection()[0]
    transaction_index = int(tree.item(selected_item)['text']) - 1
    transactions.pop(transaction_index)
    save_transactions(FILE_NAME, transactions)
    update_treeview(tree, transactions)
    update_balance(balance_label)


def update_balance(balance_label):
    global transactions
    balance = 0
    for t_type, amount, _ in transactions:
        if t_type == "income":
            balance += float(amount)
        elif t_type == "expense":
            balance -= float(amount)
    balance_label.config(text=f"Current Balance: {balance}")


def update_treeview(tree, transactions):
    for item in tree.get_children():
        tree.delete(item)
    for i, transaction in enumerate(transactions, 1):
        tree.insert('', 'end', text=i, values=transaction)


def open_file(tree, balance_label):
    global FILE_NAME
    global transactions
    file_name = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_name:
        FILE_NAME = file_name
        transactions = load_transactions(FILE_NAME)
        update_treeview(tree, transactions)
        update_balance(balance_label)


def create_new_file(tree, balance_label):
    global FILE_NAME
    global transactions
    file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_name:
        FILE_NAME = file_name
        transactions = []
        save_transactions(FILE_NAME, transactions)
        update_treeview(tree, transactions)
        update_balance(balance_label)


def main():
    global transactions
    root = tk.Tk()
    root.title("Personal Finance Tracker")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    tree = ttk.Treeview(frame, columns=('Type', 'Amount', 'Description'))
    tree.heading('#0', text='Index')
    tree.heading('#1', text='Type')
    tree.heading('#2', text='Amount (BGN)')
    tree.heading('#3', text='Description')
    tree.column('#0', width=50)
    tree.column('#1', width=100)
    tree.column('#2', width=100)
    tree.column('#3', width=200)
    tree.grid(row=0, column=0, columnspan=4)

    add_button = ttk.Button(frame, text="Add Transaction", command=lambda: add_transaction(tree, balance_label))
    add_button.grid(row=1, column=0, pady=5)

    view_button = ttk.Button(frame, text="View Transactions", command=lambda: view_transactions(tree))
    view_button.grid(row=1, column=1, pady=5)

    delete_button = ttk.Button(frame, text="Delete Transaction",
                               command=lambda: delete_transaction(tree, balance_label))
    delete_button.grid(row=1, column=2, pady=5)

    balance_label = ttk.Label(frame, text="Current Balance: 0")
    balance_label.grid(row=2, column=0, columnspan=2, pady=5)

    open_button = ttk.Button(frame, text="Open File", command=lambda: open_file(tree, balance_label))
    open_button.grid(row=3, column=0, pady=5)

    new_button = ttk.Button(frame, text="New File", command=lambda: create_new_file(tree, balance_label))
    new_button.grid(row=3, column=1, pady=5)

    transactions = load_transactions(FILE_NAME)
    update_treeview(tree, transactions)
    update_balance(balance_label)

    root.mainloop()


if __name__ == "__main__":
    main()

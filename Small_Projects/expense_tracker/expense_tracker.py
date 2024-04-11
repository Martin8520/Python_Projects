import tkinter as tk
from tkinter import messagebox
import csv


class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expenses = []

        # Expense Entry
        self.expense_label = tk.Label(master, text="Expense:")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(master, width=40)
        self.expense_entry.pack()

        # Amount Entry
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master, width=40)
        self.amount_entry.pack()

        # Category Entry
        self.category_label = tk.Label(master, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(master, width=40)
        self.category_entry.pack()

        # Add Expense Button
        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if expense and amount and category:
            self.expenses.append([expense, amount, category])
            self.save_expenses()
            messagebox.showinfo("Success", "Expense added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill out all fields.")

    def clear_entries(self):
        self.expense_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def save_expenses(self):
        with open("expenses.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Expense", "Amount", "Category"])
            writer.writerows(self.expenses)


def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.geometry("800x600")
    root.mainloop()


if __name__ == "__main__":
    main()

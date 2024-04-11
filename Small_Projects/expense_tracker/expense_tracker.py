import tkinter as tk
from tkinter import messagebox
import csv


class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expenses = []

        self.expense_label = tk.Label(master, text="Expense:")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(master, width=40)
        self.expense_entry.pack()

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master, width=40)
        self.amount_entry.pack()

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(master, width=40)
        self.category_entry.pack()

        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.expense_listbox = tk.Listbox(master, width=50)
        self.expense_listbox.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete Expense", command=self.delete_expense)
        self.delete_button.pack()

        self.edit_button = tk.Button(master, text="Edit Expense", command=self.edit_expense)
        self.edit_button.pack()

        self.load_expenses()

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if expense and amount and category:
            self.expenses.append([expense, amount, category])
            self.save_expenses()
            self.display_expenses()
            messagebox.showinfo("Success", "Expense added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill out all fields.")

    def delete_expense(self):
        try:
            selection = self.expense_listbox.curselection()[0]
            del self.expenses[selection]
            self.save_expenses()
            self.display_expenses()
        except IndexError:
            messagebox.showwarning("Warning", "Please select an expense to delete.")

    def edit_expense(self):
        try:
            selection = self.expense_listbox.curselection()[0]
            expense = self.expenses[selection]
            self.expense_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.expense_entry.insert(0, expense[0])
            self.amount_entry.insert(0, expense[1])
            self.category_entry.insert(0, expense[2])
            del self.expenses[selection]
            self.save_expenses()
            self.display_expenses()
        except IndexError:
            messagebox.showwarning("Warning", "Please select an expense to edit.")

    def clear_entries(self):
        self.expense_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def save_expenses(self):
        with open("expenses.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Expense", "Amount", "Category"])
            writer.writerows(self.expenses)

    def load_expenses(self):
        try:
            with open("expenses.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)
                self.expenses = [row for row in reader]
                self.display_expenses()
        except FileNotFoundError:
            pass

    def display_expenses(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_listbox.insert(tk.END, f"{expense[0]} - {expense[1]} - {expense[2]}")


def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.geometry("600x600")
    root.mainloop()


if __name__ == "__main__":
    main()

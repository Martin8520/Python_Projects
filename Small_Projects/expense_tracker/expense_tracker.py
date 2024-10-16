import csv
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, filedialog

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


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

        self.currency_label = tk.Label(master, text="Currency:")
        self.currency_label.pack()
        self.currency_var = tk.StringVar(master)
        self.currency_var.set("BGN")
        self.currency_menu = tk.OptionMenu(master, self.currency_var, "USD", "EUR", "GBP", "JPY", "BGN")
        self.currency_menu.pack()

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(master, width=40)
        self.category_entry.pack()

        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.xscrollbar = tk.Scrollbar(master, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.expense_listbox = tk.Listbox(master, width=70, xscrollcommand=self.xscrollbar.set)
        self.expense_listbox.pack(pady=10)

        self.xscrollbar.config(command=self.expense_listbox.xview)

        self.delete_button = tk.Button(master, text="Delete Expense", command=self.delete_expense)
        self.delete_button.pack()

        self.edit_button = tk.Button(master, text="Edit Expense", command=self.edit_expense)
        self.edit_button.pack()

        self.total_expenses_label = tk.Label(master, text="Total Expenses: BGN 0.00")
        self.total_expenses_label.pack()

        self.calculate_total_button = tk.Button(master, text="Calculate Total", command=self.calculate_total)
        self.calculate_total_button.pack()

        self.currency_var.trace_add('write', self.update_total_label)
        self.export_button = tk.Button(master, text="Export to PDF", command=self.export_to_pdf)
        self.export_button.pack()

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(master, width=40)
        self.search_entry.pack()
        self.search_button = tk.Button(master, text="Search", command=self.search_expenses)
        self.search_button.pack()
        pdfmetrics.registerFont(TTFont('Times-Roman', 'times.ttf'))
        self.load_expenses()

    def export_to_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not filename:
            return
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        header = ["Expense", "Amount", "Currency", "Category", "Date Added"]
        data = [header]
        for expense in self.expenses:
            data.append(expense)
        currency = self.currency_var.get()
        total = sum(expense[1] for expense in self.expenses)
        formatted_total = "{:.2f}".format(total)
        total_row = ["Total", formatted_total, currency, "", ""]
        data.append(total_row)
        table_data = []
        for row in data:
            table_row = []
            for item in row:
                table_row.append(str(item))
            table_data.append(table_row)
        table = Table(table_data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        table.setStyle(style)
        elements.append(table)

        doc.build(elements)
        messagebox.showinfo("Success", f"Expenses exported to {filename}")

    def calculate_total(self):
        currency = self.currency_var.get()
        total = sum(expense[1] for expense in self.expenses)
        formatted_total = "{:.2f}".format(total)
        self.total_expenses_label.config(text=f"Total Expenses: {currency} {formatted_total}")

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()
        currency = self.currency_var.get()
        category = self.category_entry.get()
        date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if expense and category:
            try:
                amount = float("{:.2f}".format(float(amount)))
                self.expenses.append([expense, amount, currency, category, date_added])
                self.save_expenses()
                self.display_expenses()
                self.clear_entries()
                self.update_total_label()
            except ValueError:
                messagebox.showwarning("Warning", "Amount must be a valid number.")
        else:
            messagebox.showwarning("Warning", "Please fill out all fields.")

    def update_total_label(self):
        currency = self.currency_var.get()
        self.total_expenses_label.config(text=f"Total Expenses: {currency} 0.00")

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
            self.currency_var.set(expense[2])
            self.category_entry.delete(0, tk.END)
            self.expense_entry.insert(0, expense[0])
            self.amount_entry.insert(0, expense[1])
            self.category_entry.insert(0, expense[3])
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
        with open("expenses.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Expense", "Amount", "Currency", "Category", "Date Added"])
            writer.writerows(self.expenses)

    def load_expenses(self):
        try:
            with open("expenses.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                self.expenses = []
                for row in reader:
                    row[1] = float(row[1])
                    self.expenses.append(row)
                self.display_expenses()
        except FileNotFoundError:
            pass

    def display_expenses(self, expenses=None):
        self.expense_listbox.delete(0, tk.END)
        if expenses is None:
            expenses = self.expenses
        for expense in expenses:
            formatted_amount = "{:.2f}".format(expense[1])
            self.expense_listbox.insert(tk.END,
                                        f"{expense[0]} - {formatted_amount} {expense[2]} - {expense[3]} ({expense[4]})")

    def search_expenses(self):
        query = self.search_entry.get().lower()
        if query:
            filtered_expenses = [expense for expense in self.expenses
                                 if query in expense[0].lower() or query in expense[3].lower()]
            self.display_expenses(filtered_expenses)
        else:
            self.display_expenses(self.expenses)


def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.geometry("500x600")
    root.mainloop()


if __name__ == "__main__":
    main()

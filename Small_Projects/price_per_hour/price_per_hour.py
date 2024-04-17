import csv
from tkinter import *
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.tasks = []
        self.total_price = 0

        self.label_task = Label(master, text="Task:")
        self.label_task.grid(row=0, column=0)

        self.label_hours = Label(master, text="Hours:")
        self.label_hours.grid(row=1, column=0)

        self.label_price = Label(master, text="Price per hour (BGN):")
        self.label_price.grid(row=2, column=0)

        self.entry_task = Entry(master)
        self.entry_task.grid(row=0, column=1)

        self.entry_hours = Entry(master)
        self.entry_hours.grid(row=1, column=1)

        self.entry_price = Entry(master)
        self.entry_price.grid(row=2, column=1)

        self.button_add_task = Button(master, text="Add Task", command=self.add_task)
        self.button_add_task.grid(row=3, column=0, columnspan=2)

        self.button_calculate_total = Button(master, text="Calculate Total", command=self.calculate_total)
        self.button_calculate_total.grid(row=4, column=0, columnspan=2)

        self.button_export_pdf = Button(master, text="Export to PDF", command=self.export_to_pdf)
        self.button_export_pdf.grid(row=5, column=0, columnspan=2)

    def add_task(self):
        task = self.entry_task.get()
        hours = self.entry_hours.get()
        price = self.entry_price.get()
        if not task:
            messagebox.showerror("Error", "Task cannot be empty.")
            return
        if hours:
            try:
                hours = float(hours)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for hours.")
                return
        else:
            hours = None
        if price:
            try:
                price = float(price)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for price.")
                return
        else:
            price = None
        self.tasks.append((task, hours, price))
        messagebox.showinfo("Success", "Task added successfully!")
        self.clear_entries()

    def calculate_total(self):
        self.total_price = sum(hours * price for _, hours, price in self.tasks if hours is not None and price is not None)
        messagebox.showinfo("Total Price", f"Total Price: {self.total_price} BGN")

    def export_to_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            c = canvas.Canvas(filename, pagesize=letter)
            c.drawString(100, 750, "Task Manager Report")
            c.drawString(100, 730, f"Total Price: {self.total_price} BGN")
            y = 700
            for task, hours, price in self.tasks:
                if hours is not None and price is not None:
                    c.drawString(100, y, f"Task: {task}, Hours: {hours}, Price per Hour: {price} BGN")
                    y -= 20
            c.save()
            messagebox.showinfo("Success", "PDF exported successfully!")

    def clear_entries(self):
        self.entry_task.delete(0, END)
        self.entry_hours.delete(0, END)
        self.entry_price.delete(0, END)

root = Tk()
app = TaskManager(root)
root.mainloop()

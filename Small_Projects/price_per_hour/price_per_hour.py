import csv
from tkinter import *
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors


class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.tasks = []
        self.total_price = 0
        self.csv_filename = ""

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

        self.button_edit_task = Button(master, text="Edit Task", command=self.edit_task)
        self.button_edit_task.grid(row=4, column=0, columnspan=2)

        self.button_export_pdf = Button(master, text="Export to PDF", command=self.export_to_pdf)
        self.button_export_pdf.grid(row=5, column=0, columnspan=2)

        self.button_create_csv = Button(master, text="Create CSV", command=self.create_csv)
        self.button_create_csv.grid(row=6, column=0, columnspan=2)

        self.button_open_csv = Button(master, text="Open CSV", command=self.open_csv)
        self.button_open_csv.grid(row=7, column=0, columnspan=2)

        self.button_save_changes = Button(master, text="Save Changes", command=self.save_changes)
        self.button_save_changes.grid(row=8, column=0, columnspan=2)

        self.task_listbox = Listbox(master, width=50, height=10)
        self.task_listbox.grid(row=9, column=0, columnspan=2)

        self.label_total_price = Label(master, text="Total Price: 0 BGN")
        self.label_total_price.grid(row=10, column=0, columnspan=2)

        self.selected_index = None

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
        self.update_task_listbox()
        self.calculate_total()
        messagebox.showinfo("Success", "Task added successfully!")
        self.clear_entries()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a task to edit.")
            return
        self.selected_index = selected_index[0]
        task, hours, price = self.tasks[self.selected_index]
        edited_task = self.entry_task.get()
        edited_hours = self.entry_hours.get()
        edited_price = self.entry_price.get()

        if edited_hours:
            try:
                edited_hours = float(edited_hours)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for hours.")
                return
        else:
            edited_hours = None

        if edited_price:
            try:
                edited_price = float(edited_price)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for price.")
                return
        else:
            edited_price = None

        self.tasks[self.selected_index] = (edited_task, edited_hours, edited_price)
        self.update_task_listbox()
        self.calculate_total()
        messagebox.showinfo("Success", "Task edited successfully!")
        self.clear_entries()

    def calculate_total(self):
        self.total_price = sum(hours * price for _, hours, price in self.tasks if hours is not None and price is not None)
        self.label_total_price.config(text=f"Total Price: {self.total_price} BGN")

    def export_to_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            doc = SimpleDocTemplate(filename)
            data = [["Task", "Hours", "Price per Hour (BGN)"]]
            for task, hours, price in self.tasks:
                if hours is not None and price is not None:
                    data.append([task, str(hours), str(price)])
            data.append(["Total Price", "", str(self.total_price) + " BGN"])
            table = Table(data)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Times-Roman'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
                                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
            doc.build([table])
            messagebox.showinfo("Success", "PDF exported successfully!")

    def create_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            self.csv_filename = filename
            self.save_changes()

    def open_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.csv_filename = filename
            self.tasks = []
            with open(self.csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    task = row[0]
                    hours = float(row[1]) if row[1] else None
                    price = float(row[2]) if row[2] else None
                    self.tasks.append((task, hours, price))
            self.update_task_listbox()
            self.calculate_total()
            messagebox.showinfo("Success", f"CSV file '{filename}' opened successfully!")

    def save_changes(self):
        if not self.csv_filename:
            messagebox.showerror("Error", "No CSV file has been created or opened.")
            return
        with open(self.csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Task', 'Hours', 'Price per hour (BGN)'])
            for task, hours, price in self.tasks:
                csv_writer.writerow([task, hours if hours is not None else '', price if price is not None else ''])
        messagebox.showinfo("Success", "Changes saved successfully!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task, hours, price in self.tasks:
            self.task_listbox.insert(END, f"Task: {task}, Hours: {hours if hours is not None else 'N/A'}, Price per Hour: {price if price is not None else 'N/A'} BGN")

    def clear_entries(self):
        self.entry_task.delete(0, END)
        self.entry_hours.delete(0, END)
        self.entry_price.delete(0, END)

root = Tk()
app = TaskManager(root)
root.mainloop()

import csv
from tkinter import *
from tkinter import filedialog, messagebox
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import datetime


class Task:
    def __init__(self, task="", hours=None, price=None, start_date="", end_date=""):
        self.task = task
        self.hours = hours
        self.price = price
        self.start_date = start_date
        self.end_date = end_date


class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Price/Hours Calculator")

        self.tasks = []
        self.total_price = 0
        self.csv_filename = ""
        self.language = "bulgarian"

        self.language_var = StringVar()
        self.language_var.set("Bulgarian")
        self.language_menu = OptionMenu(master, self.language_var, "English", "Bulgarian", command=self.change_language)
        self.language_menu.config(width=12)
        self.language_menu.grid(row=0, column=0, columnspan=1, sticky="w", padx=5, pady=5)

        self.label_task = Label(master, text="Задача:" if self.language == "bulgarian" else "Task:")
        self.label_task.grid(row=1, column=0, sticky='e', padx=(0, 10))

        self.label_hours = Label(master, text="Часове:" if self.language == "bulgarian" else "Hours:")
        self.label_hours.grid(row=2, column=0, sticky='e', padx=(0, 10))

        self.label_price = Label(master, text="Цена на час в BGN:" if self.language == "bulgarian" else "Price per hour in BGN:")
        self.label_price.grid(row=3, column=0, sticky='e', padx=(0, 10))

        self.entry_task = Entry(master)
        self.entry_task.grid(row=1, column=1, sticky='w')

        self.entry_hours = Entry(master)
        self.entry_hours.grid(row=2, column=1, sticky='w')

        self.entry_price = Entry(master)
        self.entry_price.grid(row=3, column=1, sticky='w')

        self.button_add_task = Button(master, text="Добави Задача" if self.language == "bulgarian" else "Add Task", command=self.add_task, width=15, height=1,
                                      anchor='w', justify='left')
        self.button_add_task.grid(row=4, column=0, columnspan=1, sticky='w', padx=(10, 0), pady=5)

        self.button_edit_task = Button(master, text="Промени Задача" if self.language == "bulgarian" else "Edit Task", command=self.edit_task, width=15, height=1,
                                       anchor='w', justify='left')
        self.button_edit_task.grid(row=5, column=0, columnspan=1, sticky='w', padx=(10, 0), pady=5)

        self.button_export_pdf = Button(master, text="Запази в PDF" if self.language == "bulgarian" else "Save to PDF", command=self.export_to_pdf, width=15, height=1,
                                        anchor='w', justify='left')
        self.button_export_pdf.grid(row=6, column=0, columnspan=1, sticky='w', padx=(10, 0), pady=5)

        self.button_create_csv = Button(master, text="Създай нов файл" if self.language == "bulgarian" else "Create new file", command=self.create_csv, width=15, height=1,
                                        anchor='e', justify='right')
        self.button_create_csv.grid(row=4, column=1, columnspan=1, sticky='e', padx=(0, 10), pady=5)

        self.button_open_csv = Button(master, text="Отвори файл" if self.language == "bulgarian" else "Open file", command=self.open_csv, width=15, height=1, anchor='e',
                                      justify='right')
        self.button_open_csv.grid(row=5, column=1, columnspan=1, sticky='e', padx=(0, 10), pady=5)

        self.button_save_changes = Button(master, text="Запази" if self.language == "bulgarian" else "Save", command=self.save_changes, width=15, height=1,
                                          anchor='e', justify='right')
        self.button_save_changes.grid(row=6, column=1, columnspan=1, sticky='e', padx=(0, 10), pady=5)

        self.button_delete_task = Button(master, text="Изтрий Задача" if self.language == "bulgarian" else "Delete Task", command=self.delete_task, width=15, height=1,
                                         bg="#ff6666", anchor='w', justify='left')
        self.button_delete_task.grid(row=11, column=0, columnspan=2, sticky='w', padx=(10, 0), pady=5)

        self.button_mark_completed = Button(master, text="Маркирай като завършена" if self.language == "bulgarian" else "Mark as completed", command=self.mark_completed,
                                            width=21, height=1, anchor='e', justify='right', bg="#a6ffb4")
        self.button_mark_completed.grid(row=11, column=1, columnspan=1, sticky='e', padx=(0, 10), pady=5)

        self.task_listbox = Listbox(master, width=100, height=10)
        self.task_listbox.grid(row=9, column=0, columnspan=2, sticky='nsew', padx=(10, 0))
        self.task_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.label_total_price = Label(master, text="Обща цена: 0 лв." if self.language == "bulgarian" else "Total price: 0 BGN")
        self.label_total_price.grid(row=10, column=0, columnspan=2, sticky='w', padx=(10, 0))

        self.selected_index = None

        master.grid_rowconfigure(9, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

    def change_language(self, event):
        self.language = self.language_var.get().lower()
        self.update_ui_language()

    def update_ui_language(self):
        if self.language == "bulgarian":
            self.label_task.config(text="Задача:")
            self.label_hours.config(text="Часове:")
            self.label_price.config(text="Цена на час в BGN:")
            self.button_add_task.config(text="Добави Задача")
            self.button_edit_task.config(text="Промени Задача")
            self.button_export_pdf.config(text="Запази в PDF")
            self.button_create_csv.config(text="Създай нов файл")
            self.button_open_csv.config(text="Отвори файл")
            self.button_save_changes.config(text="Запази")
            self.button_delete_task.config(text="Изтрий Задача")
            self.button_mark_completed.config(text="Маркирай като завършена")
            self.label_total_price.config(text="Обща цена: 0 лв.")
        else:
            self.label_task.config(text="Task:")
            self.label_hours.config(text="Hours:")
            self.label_price.config(text="Price per hour in BGN:")
            self.button_add_task.config(text="Add Task")
            self.button_edit_task.config(text="Edit Task")
            self.button_export_pdf.config(text="Save to PDF")
            self.button_create_csv.config(text="Create new file")
            self.button_open_csv.config(text="Open file")
            self.button_save_changes.config(text="Save")
            self.button_delete_task.config(text="Delete Task")
            self.button_mark_completed.config(text="Mark as completed")
            self.label_total_price.config(text="Total price: 0 BGN")

    def on_entry_focus(self, event):
        self.selected_index = self.task_listbox.curselection()

    def on_select(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
            task = self.tasks[self.selected_index]
            self.entry_task.delete(0, END)
            self.entry_task.insert(END, task.task)
            self.entry_hours.delete(0, END)
            self.entry_hours.insert(END, str(task.hours) if task.hours is not None else "")
            self.entry_price.delete(0, END)
            self.entry_price.insert(END, str(task.price) if task.price is not None else "")

    def add_task(self):
        task = Task(
            self.entry_task.get(),
            float(self.entry_hours.get()) if self.entry_hours.get() else None,
            float(self.entry_price.get()) if self.entry_price.get() else None,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            ""
        )
        if not task.task:
            messagebox.showerror("Грешка", "Задачата трябва да има име.")
            return
        self.tasks.append(task)
        self.update_task_listbox()
        self.calculate_total()
        self.clear_entries()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Грешка", "Моля изберете задачата, която искате да редактирате.")
            return

        task = self.tasks[selected_index[0]]

        edit_window = Toplevel(self.master)
        edit_window.title("Редактиране на Задача")

        edit_window.grid_rowconfigure(0, weight=1)
        edit_window.grid_rowconfigure(1, weight=1)
        edit_window.grid_rowconfigure(2, weight=1)
        edit_window.grid_columnconfigure(0, weight=1)
        edit_window.grid_columnconfigure(1, weight=1)

        if self.language == "bulgarian":
            Label(edit_window, text="Задача:").grid(row=0, column=0, sticky='e')
            Label(edit_window, text="Часове:").grid(row=1, column=0, sticky='e')
            Label(edit_window, text="Цена на час в лева:").grid(row=2, column=0, sticky='e')
            save_button_text = "Запази"
            cancel_button_text = "Откажи"
        else:
            Label(edit_window, text="Task:").grid(row=0, column=0, sticky='e')
            Label(edit_window, text="Hours:").grid(row=1, column=0, sticky='e')
            Label(edit_window, text="Price per hour in BGN:").grid(row=2, column=0, sticky='e')
            save_button_text = "Save"
            cancel_button_text = "Cancel"

        entry_task = Entry(edit_window)
        entry_task.grid(row=0, column=1, sticky='we')
        entry_task.insert(END, task.task)

        entry_hours = Entry(edit_window)
        entry_hours.grid(row=1, column=1, sticky='we')
        entry_hours.insert(END, str(task.hours) if task.hours is not None else "")

        entry_price = Entry(edit_window)
        entry_price.grid(row=2, column=1, sticky='we')
        entry_price.insert(END, str(task.price) if task.price is not None else "")

        def save_edit():
            task.task = entry_task.get()
            task.hours = float(entry_hours.get()) if entry_hours.get() else None
            task.price = float(entry_price.get()) if entry_price.get() else None

            self.update_task_listbox()
            self.calculate_total()

            edit_window.destroy()

        for child_e in edit_window.winfo_children():
            child_e.grid_configure(padx=5, pady=5)

        edit_window.update_idletasks()
        button_frame = Frame(edit_window)
        button_frame.grid(row=5, column=0, columnspan=2, sticky='nsew')
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        Button(button_frame, text=save_button_text, command=save_edit).pack(side=LEFT, padx=5, pady=10)
        Button(button_frame, text=cancel_button_text, command=edit_window.destroy).pack(side=RIGHT, padx=5, pady=10)

        edit_window.geometry("")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Грешка", "Моля селектирайте задачата, която искате да маркирате като завършена.")
            return
        task = self.tasks[selected_index[0]]
        task.end_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.update_task_listbox()
        self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(
            (task.hours * task.price) if (task.hours is not None and task.price is not None) else 0 for task in
            self.tasks)
        self.label_total_price.config(text=f"Обща цена: {self.total_price} лв.")

    def export_to_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            doc = SimpleDocTemplate(filename)

            pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

            data = [["Задача", "Часове", "Цена на час в лева", "Дата на започване", "Дата на завършване"]]
            for task in self.tasks:
                if task.hours is not None and task.price is not None:
                    data.append([task.task, str(task.hours), str(task.price), task.start_date, task.end_date])
            data.append(["Обща цена", "", str(self.total_price) + " лв.", "", ""])

            table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                      ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                      ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                      ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                      ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
                                      ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                      ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12)])

            table = Table(data)
            table.setStyle(table_style)
            doc.build([table])

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
                    task = Task(
                        row[0],
                        float(row[1]) if row[1] else None,
                        float(row[2]) if row[2] else None,
                        row[3],
                        row[4]
                    )
                    self.tasks.append(task)
            self.update_task_listbox()
            self.calculate_total()

    def save_changes(self):
        if not self.csv_filename:
            messagebox.showerror("Грешка", "Няма създаден или отворен CSV файл.")
            return
        with open(self.csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Задача', 'Часове', 'Цена на час в лева', 'Дата на започване', 'Дата на завършване'])
            for task in self.tasks:
                csv_writer.writerow([task.task, task.hours if task.hours is not None else '',
                                     task.price if task.price is not None else '',
                                     task.start_date, task.end_date])

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            return
        del self.tasks[selected_index[0]]
        self.update_task_listbox()
        self.calculate_total()
        if self.csv_filename:
            self.save_changes()

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            task_text = f"Задача: {task.task}"
            if task.hours is not None:
                task_text += f", Часове: {task.hours}"
            if task.price is not None:
                task_text += f", Цена на час в лева: {task.price} лв."
            task_text += f", Дата на започване: {task.start_date}"
            if task.end_date:
                task_text += f", Дата на завършване: {task.end_date}"
            else:
                task_text += ", Незавършена"
            self.task_listbox.insert(END, task_text)
            if task.end_date:
                self.task_listbox.itemconfig(END, {'bg': '#a6ffb4'})
            else:
                self.task_listbox.itemconfig(END, {'bg': '#ff6666'})

    def clear_entries(self):
        self.entry_task.delete(0, END)
        self.entry_hours.delete(0, END)
        self.entry_price.delete(0, END)


root = Tk()
app = TaskManager(root)
window_width = 800
window_height = 550

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)
root.mainloop()

import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление на задачи")
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", self.on_frame_configure)

        self.tasks = []
        self.create_file_button = ttk.Button(root, text="Създай нов файл", command=self.create_new_file)
        self.create_file_button.pack(pady=10)
        self.open_file_button = ttk.Button(root, text="Отвори съществуващ файл", command=self.open_existing_file)
        self.open_file_button.pack(pady=10)
        self.export_pdf_button = ttk.Button(root, text="Export to PDF", command=self.export_to_pdf)
        self.export_pdf_button.pack(pady=10)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_new_file(self):
        self.file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.file_name:
            self.save_tasks()
            self.setup_ui()

    def open_existing_file(self):
        self.file_name = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.file_name:
            self.load_tasks()
            self.canvas.delete("all")
            self.frame.destroy()
            self.frame = ttk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
            self.setup_ui()

    def load_tasks(self):
        self.tasks.clear()
        try:
            with open(self.file_name, mode="r", newline="", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = {
                        "Task": row.get("Задача", ""),
                        "Status": row.get("Статус", ""),
                        "Price (BGN)": row.get("Цена (BGN)", ""),
                        "Start Date": row.get("Начална дата", ""),
                        "End Date": row.get("Крайна дата", "")
                    }
                    self.tasks.append(task)
        except Exception as e:
            print("Грешка при зареждане на задачите:", e)

    def save_tasks(self):
        with open(self.file_name, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=["Задача", "Статус", "Цена (BGN)", "Начална дата", "Крайна дата"])
            writer.writeheader()
            for task in self.tasks:
                task_data = {
                    "Задача": task["Task"],
                    "Статус": task["Status"],
                    "Цена (BGN)": task.get("Price (BGN)", ""),
                    "Начална дата": task["Start Date"],
                    "Крайна дата": task["End Date"]
                }
                writer.writerow(task_data)

    def setup_ui(self):
        self.clear_ui()
        self.price_entries = []
        add_task_button = ttk.Button(self.frame, text="Добави задача", command=self.add_task)
        add_task_button.pack(pady=10)
        for task_index, task in enumerate(self.tasks):
            task_frame = ttk.Frame(self.frame)
            task_frame.pack(padx=10, pady=5, fill="x")
            task_text = tk.Text(task_frame, height=3, width=50)
            task_text.insert("1.0", task.get("Task", ""))
            task_text.pack(side="left", padx=5)
            status_var = tk.StringVar(value=task.get("Status", ""))
            status_combobox = ttk.Combobox(task_frame, values=["Не е започната", "Започната", "Завършена", "Одобрена"],
                                           textvariable=status_var)
            status_combobox.pack(side="left", padx=5)
            price_label = ttk.Label(task_frame, text="Цена (BGN):")
            price_label.pack(side="left", padx=5)
            price_var = tk.StringVar(value=task.get("Price (BGN)", ""))
            price_entry = ttk.Entry(task_frame, textvariable=price_var)
            price_entry.pack(side="left", padx=5)
            self.price_entries.append(price_entry)
            start_date_label = ttk.Label(task_frame, text="Начална дата:")
            start_date_label.pack(side="left", padx=5)
            start_date_text = task.get("Start Date", "")
            start_date_label_value = ttk.Label(task_frame, text=start_date_text)
            start_date_label_value.pack(side="left", padx=5)
            end_date_label = ttk.Label(task_frame, text="Крайна дата:")
            end_date_label.pack(side="left", padx=5)
            end_date_text = task.get("End Date", "")
            end_date_label_value = ttk.Label(task_frame, text=end_date_text)
            end_date_label_value.pack(side="left", padx=5)
            edit_date_button = ttk.Button(task_frame, text="Промени дата",
                                           command=lambda index=task_index: self.edit_date(index))
            edit_date_button.pack(side="right", padx=5)
            delete_button = ttk.Button(task_frame, text="Изтрий",
                                       command=lambda index=task_index: self.delete_task(index))
            delete_button.pack(side="right", padx=5)
            task_ = task
            status_var_ = status_var
            price_var_ = price_var
            status_combobox.bind("<<ComboboxSelected>>", lambda event, task=task_, status_var=status_var_,
                                                                price_var=price_var_: self.update_status(event, task,
                                                                                                         status_var,
                                                                                                         price_var))
            task_text.config(state="normal")
            task_text.bind("<FocusOut>",
                           lambda event, task_index=task_index, task=task, task_text=task_text: self.update_task_text(
                               event, task_index, task, task_text))

        save_changes_button = ttk.Button(self.frame, text="Запази промените", command=self.save_changes)
        save_changes_button.pack(pady=10)
        calculate_total_button = ttk.Button(self.frame, text="Изчисли общо", command=self.calculate_total)
        calculate_total_button.pack(pady=10)
        total_price_var = tk.StringVar()
        total_price_label = ttk.Label(self.frame, text="Обща цена: ", textvariable=total_price_var)
        total_price_label.pack(side="left", padx=5)
        self.total_price_var = total_price_var
        self.update_total_price()
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def export_to_pdf(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, "fonts", "arial-unicode-ms.ttf")

        pdfmetrics.registerFont(TTFont('CustomFont', font_path))

        pdf_file_name = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_file_name:
            doc = SimpleDocTemplate(pdf_file_name, pagesize=letter)
            data = [["Задача", "Статус", "Цена (BGN)", "Начална дата", "Крайна дата"]]
            total_price = 0

            for task in self.tasks:
                data.append([task["Task"], task["Status"], task.get("Price (BGN)", ""),
                             task["Start Date"], task["End Date"]])
                if task.get("Price (BGN)"):
                    total_price += float(task["Price (BGN)"])

            data.append(["Обща цена", "", f"{total_price} BGN", "", ""])

            table_style = [
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 0), (-1, -1), 'CustomFont'),
            ]

            table = Table(data)
            table.setStyle(TableStyle(table_style))

            doc.build([table])

    def save_changes(self):
        edited_tasks = []
        for task_frame in self.frame.winfo_children():
            if isinstance(task_frame, ttk.Frame):
                task_text = task_frame.winfo_children()[0]
                price_entry = task_frame.winfo_children()[3]
                task_name = task_text.get("1.0", "end-1c").strip()
                price = price_entry.get().strip()
                edited_tasks.append((task_name, price))

        for task in self.tasks:
            for edited_task in edited_tasks:
                if edited_task[0] == task["Task"]:
                    task["Price (BGN)"] = edited_task[1]

        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()
        self.setup_ui()

    def add_task(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавяне на задача")
        task_label = ttk.Label(dialog, text="Задача:")
        task_label.pack(pady=5)
        task_entry = tk.Text(dialog, height=3, width=50)
        task_entry.pack(padx=10, pady=5)
        price_label = ttk.Label(dialog, text="Цена (BGN):")
        price_label.pack(pady=5)
        price_var = tk.StringVar()
        price_entry = ttk.Entry(dialog, textvariable=price_var)
        price_entry.pack(pady=5)
        start_date = datetime.now().strftime("%d/%m/%Y %H:%M")

        def add_task_to_list():
            task_name = task_entry.get("1.0", "end-1c")
            price = price_var.get()
            if task_name:
                new_task = {
                    "Task": task_name,
                    "Status": "Не е започната",
                    "Price (BGN)": price,
                    "Start Date": start_date,
                    "End Date": ""
                }
                self.tasks.append(new_task)
                self.save_tasks()
                self.setup_ui()
                dialog.destroy()

        add_button = ttk.Button(dialog, text="Добави задача", command=add_task_to_list)
        add_button.pack(pady=10)

    def edit_date(self, index):
        task = self.tasks[index]
        dialog = tk.Toplevel(self.root)
        dialog.title("Промяна на дата")
        start_date_label = ttk.Label(dialog, text="Начална дата:")
        start_date_label.pack(pady=5)
        start_date_var = tk.StringVar(value=task["Start Date"])
        start_date_entry = ttk.Entry(dialog, textvariable=start_date_var)
        start_date_entry.pack(pady=5)
        end_date_label = ttk.Label(dialog, text="Крайна дата:")
        end_date_label.pack(pady=5)
        end_date_var = tk.StringVar(value=task["End Date"])
        end_date_entry = ttk.Entry(dialog, textvariable=end_date_var)
        end_date_entry.pack(pady=5)

        def save_date_changes():
            task["Start Date"] = start_date_var.get().strip()
            task["End Date"] = end_date_var.get().strip()
            self.save_tasks()
            self.setup_ui()
            dialog.destroy()

        save_button = ttk.Button(dialog, text="Запази", command=save_date_changes)
        save_button.pack(pady=10)

    def clear_ui(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def update_status(self, event, task, status_var, price_var):
        new_status = status_var.get()
        new_price = price_var.get().strip()
        if (new_status == "Завършена" or new_status == "Одобрена") and not task["End Date"]:
            task["Status"] = new_status
            task["End Date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
        else:
            task["Status"] = new_status
        task["Price (BGN)"] = new_price if new_price else task.get("Price (BGN)", "")
        self.save_tasks()
        self.setup_ui()

    def calculate_total(self):
        total = sum(float(task_entry.get()) for task_entry in self.price_entries if task_entry.get().strip())
        self.total_price_var.set(f"{total} BGN")

    def update_task_text(self, event, task_index, task, task_text):
        new_value = task_text.get("1.0", "end-1c").strip()
        task["Task"] = new_value

    def update_total_price(self):
        total = sum(float(task_entry.get()) for task_entry in self.price_entries if task_entry.get().strip())
        self.total_price_var.set(f"{total} BGN")


root = tk.Tk()
root.geometry("1600x600")
app = TaskManager(root)
root.mainloop()

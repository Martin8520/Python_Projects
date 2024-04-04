import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
import csv


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление на задачи")
        self.tasks = []
        self.create_file_button = ttk.Button(root, text="Създай нов файл", command=self.create_new_file)
        self.create_file_button.pack(pady=10)
        self.open_file_button = ttk.Button(root, text="Отвори съществуващ файл", command=self.open_existing_file)
        self.open_file_button.pack(pady=10)

    def create_new_file(self):
        self.file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.file_name:
            self.save_tasks()
            self.setup_ui()

    def open_existing_file(self):
        self.file_name = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.file_name:
            self.load_tasks()
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
                        "Time Added": row.get("Време на добавяне", ""),
                        "Time Completed": row.get("Време на завършване", ""),
                        "Price (BGN)": row.get("Цена (BGN)", ""),
                        "Start Date": row.get("Начална дата", ""),
                        "End Date": row.get("Крайна дата", ""),
                    }
                    self.tasks.append(task)
        except Exception as e:
            print("Грешка при зареждане на задачите:", e)

    def save_tasks(self):
        with open(self.file_name, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=["Задача", "Статус", "Време на добавяне", "Време на завършване",
                                                      "Цена (BGN)", "Начална дата", "Крайна дата"])
            writer.writeheader()
            for task in self.tasks:
                task_data = {
                    "Задача": task["Task"],
                    "Статус": task["Status"],
                    "Време на добавяне": task.get("Time Added", ""),  # Adjust for missing key
                    "Време на завършване": task.get("Time Completed", ""),  # Adjust for missing key
                    "Цена (BGN)": task.get("Price (BGN)", ""),  # Adjust for missing key
                    "Начална дата": task["Start Date"],
                    "Крайна дата": task["End Date"]
                }
                writer.writerow(task_data)

    def setup_ui(self):
        self.clear_ui()
        self.price_entries = []
        add_task_button = ttk.Button(self.root, text="Добави задача", command=self.add_task)
        add_task_button.pack(pady=10)
        for task_index, task in enumerate(self.tasks):
            task_frame = ttk.Frame(self.root)
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
            task_ = task
            price_var_ = price_var
            price_entry.bind("<FocusOut>",
                             lambda event, task=task_, price_var=price_var_: self.update_price(event, task, price_var))
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

            task_frame.pack(fill="x", padx=10, pady=5)
        save_changes_button = ttk.Button(self.root, text="Запази промените", command=self.save_changes)
        save_changes_button.pack(pady=10)
        calculate_total_button = ttk.Button(self.root, text="Изчисли общо", command=self.calculate_total)
        calculate_total_button.pack(pady=10)
        total_price_label = ttk.Label(self.root, text="Обща цена: ")
        total_price_label.pack(side="left", padx=5)
        self.total_price_var = tk.StringVar()
        total_price_entry = ttk.Entry(self.root, textvariable=self.total_price_var, state="readonly", width=10)
        total_price_entry.pack(side="left", padx=5)
        self.update_total_price()

    def save_changes(self):
        for task in self.tasks:
            for task_frame in self.root.winfo_children():
                if isinstance(task_frame, ttk.Frame):
                    task_text = task_frame.winfo_children()[0]
                    if task_text.get("1.0", "end-1c") == task["Task"]:
                        task["Task"] = task_text.get("1.0", "end-1c").strip()
        self.save_tasks()
        self.setup_ui()

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
                    "Time Added": start_date,
                    "Time Completed": "",
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

    def clear_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_file_button = ttk.Button(self.root, text="Създай нов файл", command=self.create_new_file)
        self.create_file_button.pack(pady=10)
        self.open_file_button = ttk.Button(self.root, text="Отвори съществуващ файл", command=self.open_existing_file)
        self.open_file_button.pack(pady=10)

    def update_status(self, event, task, status_var, price_var):
        new_status = status_var.get()
        new_price = price_var.get().strip()
        if (new_status == "Завършена" or new_status == "Одобрена") and not task["Time Completed"]:
            task["Status"] = new_status
            task["Time Completed"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            task["End Date"] = task["Time Completed"]
        else:
            task["Status"] = new_status
        task["Price (BGN)"] = new_price if new_price else task.get("Price (BGN)", "")
        self.save_tasks()
        self.setup_ui()

    def calculate_total(self):
        total = sum(float(task_entry.get()) for task_entry in self.price_entries if task_entry.get().strip())
        self.total_price_var.set(f"{total} BGN")

    def update_price(self, event, task, price_var):
        new_price = price_var.get().strip()
        task["Price (BGN)"] = new_price if new_price else task.get("Price (BGN)", "")
        self.save_tasks()

    def update_task_text(self, event, task_index, task, task_text):
        new_value = task_text.get("1.0", "end-1c").strip()
        task["Task"] = new_value

    def update_total_price(self):
        total = sum(float(task_entry.get()) for task_entry in self.price_entries if task_entry.get().strip())
        self.total_price_var.set(f"{total} BGN")


root = tk.Tk()
root.geometry("1400x600")
app = TaskManager(root)
root.mainloop()

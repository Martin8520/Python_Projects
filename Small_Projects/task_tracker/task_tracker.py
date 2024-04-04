import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
import csv

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []

        self.create_file_button = ttk.Button(root, text="Create New File", command=self.create_new_file)
        self.create_file_button.pack(pady=10)

        self.open_file_button = ttk.Button(root, text="Open Existing File", command=self.open_existing_file)
        self.open_file_button.pack(pady=10)

    def create_new_file(self):
        self.file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.file_name:
            self.tasks = []
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
            with open(self.file_name, mode="r") as file:
                print("File contents:")
                file.seek(0)
                reader = csv.DictReader(file)
                for row in reader:
                    self.tasks.append(row)
        except Exception as e:
            print("Error loading tasks:", e)

    def setup_ui(self):
        self.clear_ui()

        add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.pack(pady=10)

        for task in self.tasks:
            task_frame = ttk.Frame(self.root)
            task_frame.pack(padx=10, pady=5, fill="x")

            task_text = tk.Text(task_frame, height=3, width=50)
            task_text.insert("1.0", task.get("Task", ""))
            task_text.pack(side="left", padx=5)

            status_var = tk.StringVar(value=task.get("Status", ""))
            status_combobox = ttk.Combobox(task_frame, values=["Not started", "Started", "Completed", "Approved"],
                                           textvariable=status_var)
            status_combobox.pack(side="left", padx=5)

            status_combobox.bind("<<ComboboxSelected>>",
                                 lambda event, task=task, status_var=status_var: self.update_status(task, status_var))

            task_text.config(state="normal")

    def add_task(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Task")

        task_entry = tk.Text(dialog, height=10, width=50)
        task_entry.pack(padx=10, pady=10)

        def add_task_to_list():
            task_name = task_entry.get("1.0", "end-1c")
            if task_name:
                new_task = {"Task": task_name, "Status": "Not started",
                            "Time Added": datetime.now().strftime("%d/%m/%Y %H:%M"), "Time Completed": ""}
                self.tasks.append(new_task)
                self.save_tasks()
                self.setup_ui()
                dialog.destroy()

        add_button = ttk.Button(dialog, text="Add Task", command=add_task_to_list)
        add_button.pack(pady=10)

    def clear_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_file_button = ttk.Button(self.root, text="Create New File", command=self.create_new_file)
        self.create_file_button.pack(pady=10)

        self.open_file_button = ttk.Button(self.root, text="Open Existing File", command=self.open_existing_file)
        self.open_file_button.pack(pady=10)

    def update_status(self, task, status_var):
        new_status = status_var.get()
        if (new_status == "Completed" or new_status == "Approved") and not task["Time Completed"]:
            task["Status"] = new_status
            task["Time Completed"] = datetime.now().strftime("%d/%m/%Y %H:%M")
        else:
            task["Status"] = new_status
        self.save_task()
        self.setup_ui()

    def save_tasks(self):
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task", "Status", "Time Added", "Time Completed"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task)


root = tk.Tk()
app = TaskManager(root)
root.mainloop()

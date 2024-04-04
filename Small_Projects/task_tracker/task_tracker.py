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
            self.add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
            self.add_task_button.pack(pady=10)

            self.task_label = ttk.Label(self.root, text="Task:")
            self.task_label.pack()
            self.task_entry = ttk.Entry(self.root)
            self.task_entry.pack()

            self.status_label = ttk.Label(self.root, text="Status:")
            self.status_label.pack()
            self.status_combobox = ttk.Combobox(self.root, values=["Not started", "Started", "Completed", "Approved"])
            self.status_combobox.pack()

            self.save_button = ttk.Button(self.root, text="Save", command=self.save_task)
            self.save_button.pack(pady=10)

    def open_existing_file(self):
        self.file_name = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.file_name:
            self.load_tasks()

    def load_tasks(self):
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tasks.append(row)

    def add_task(self):
        task = self.task_entry.get()
        status = self.status_combobox.get()
        time_added = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.tasks.append({"Task": task, "Status": status, "Time Added": time_added})

    def save_task(self):
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task", "Status", "Time Added", "Time Completed"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task)

root = tk.Tk()
app = TaskManager(root)
root.mainloop()

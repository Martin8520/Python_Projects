import tkinter as tk
from tkinter import ttk, filedialog, messagebox
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
            self.save_tasks()  # Save an empty list of tasks to the new file
            self.setup_ui()

    def open_existing_file(self):
        self.file_name = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        print("File name:", self.file_name)  # Debug print
        if self.file_name:
            self.load_tasks()
            self.setup_ui()

    def load_tasks(self):
        self.tasks.clear()
        try:
            with open(self.file_name, mode="r") as file:
                print("File contents:")
                print(file.read())  # Debug print
                file.seek(0)  # Reset file pointer to beginning
                reader = csv.DictReader(file)
                print("Fieldnames:", reader.fieldnames)  # Debug print
                for row in reader:
                    print("Loaded task:", row)  # Debug print
                    self.tasks.append(row)
            print("Tasks loaded:", self.tasks)  # Debug print
            print("Number of tasks loaded:", len(self.tasks))  # Debug print
        except Exception as e:
            print("Error loading tasks:", e)

    def save_tasks(self):
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task", "Status", "Time Added", "Time Completed", "Price (BGN)", "Start Date", "End Date"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task)

    def setup_ui(self):
        self.clear_ui()

        add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.pack(pady=10)

        # Initialize last_added_price to 0
        last_added_price = 0

        # Get the last added price if available
        if self.tasks:
            last_added_price = self.tasks[-1].get("Price (BGN)", 0)

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

            price_label = ttk.Label(task_frame, text="Price (BGN):")
            price_label.pack(side="left", padx=5)

            # Set initial value of price field to last added price or 0
            price_var = tk.StringVar(value=last_added_price)
            price_entry = ttk.Entry(task_frame, textvariable=price_var)
            price_entry.pack(side="left", padx=5)

            start_date_label = ttk.Label(task_frame, text="Start Date:")
            start_date_label.pack(side="left", padx=5)

            start_date_text = task.get("Start Date", "")
            start_date_label_value = ttk.Label(task_frame, text=start_date_text)
            start_date_label_value.pack(side="left", padx=5)

            end_date_label = ttk.Label(task_frame, text="End Date:")
            end_date_label.pack(side="left", padx=5)

            end_date_text = task.get("End Date", "")
            end_date_label_value = ttk.Label(task_frame, text=end_date_text)
            end_date_label_value.pack(side="left", padx=5)

            status_combobox.bind("<<ComboboxSelected>>",
                                 lambda event, task=task, status_var=status_var: self.update_status(task, status_var))

            task_text.config(state="normal")

            # Pack the task frame containing all widgets
            task_frame.pack(fill="x", padx=10, pady=5)

        calculate_total_button = ttk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        calculate_total_button.pack(pady=10)

    def add_task(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Task")

        task_label = ttk.Label(dialog, text="Task:")
        task_label.pack(pady=5)

        task_entry = tk.Text(dialog, height=3, width=50)
        task_entry.pack(padx=10, pady=5)

        price_label = ttk.Label(dialog, text="Price (BGN):")
        price_label.pack(pady=5)

        price_entry = ttk.Entry(dialog)
        price_entry.pack(pady=5)

        # Automatically set the start date
        start_date = datetime.now().strftime("%d/%m/%Y %H:%M")

        def add_task_to_list():
            task_name = task_entry.get("1.0", "end-1c")
            if task_name:
                new_task = {
                    "Task": task_name,
                    "Status": "Not started",
                    "Time Added": start_date,  # Set the start date
                    "Time Completed": "",
                    "Price (BGN)": price_entry.get(),
                    "Start Date": start_date,  # Set the start date
                    "End Date": ""
                }
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
        if new_status in ["Completed", "Approved"]:
            task["Status"] = new_status
            task["Time Completed"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            task["End Date"] = task["Time Completed"]  # Set end date to the time completed
        else:
            task["Status"] = new_status
        self.save_tasks()
        self.setup_ui()

    def calculate_total(self):
        total = sum(float(task.get("Price (BGN)", 0)) for task in self.tasks if task.get("Price (BGN)").strip())
        messagebox.showinfo("Total Sum", f"Total Sum of Tasks: {total} BGN")


root = tk.Tk()
app = TaskManager(root)
root.mainloop()

import json
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, filedialog, ttk


class TaskManager:
    def __init__(self, tasks_filename='tasks.json', completed_tasks_filename='completed_tasks.json'):
        self.tasks_filename = tasks_filename
        self.completed_tasks_filename = completed_tasks_filename
        self.tasks = []
        self.completed_tasks = []
        self.last_completed_date = None
        self.current_streak = 0
        self.load_tasks()
        self.load_completed_tasks()

    def load_tasks(self, filename=None):
        if filename:
            self.tasks_filename = filename
        if os.path.exists(self.tasks_filename):
            with open(self.tasks_filename, 'r') as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def load_completed_tasks(self, filename=None):
        if filename:
            self.completed_tasks_filename = filename
        if os.path.exists(self.completed_tasks_filename):
            with open(self.completed_tasks_filename, 'r') as file:
                try:
                    data = json.load(file)
                    if isinstance(data, dict):
                        self.completed_tasks = data.get('completed_tasks', [])
                        self.last_completed_date = data.get('last_completed_date')
                        self.current_streak = data.get('current_streak', 0)
                    else:
                        self.completed_tasks = []
                        self.last_completed_date = None
                        self.current_streak = 0
                except json.JSONDecodeError:
                    self.completed_tasks = []
                    self.last_completed_date = None
                    self.current_streak = 0
        else:
            self.completed_tasks = []
            self.last_completed_date = None
            self.current_streak = 0

    def save_tasks(self):
        with open(self.tasks_filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def save_completed_tasks(self):
        with open(self.completed_tasks_filename, 'w') as file:
            data = {
                'completed_tasks': self.completed_tasks,
                'last_completed_date': self.last_completed_date,
                'current_streak': self.current_streak
            }
            json.dump(data, file, indent=4)

    def add_task(self, task, points):
        self.tasks.append({'task': task, 'points': points})
        self.save_tasks()

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.completed_tasks.append({'task': task['task'], 'points': task['points'], 'timestamp': timestamp})
            self.update_streak()
            self.save_completed_tasks()
            return task['points']
        return 0

    def update_streak(self):
        today = datetime.today().date()
        if self.last_completed_date:
            last_date = datetime.strptime(self.last_completed_date, "%Y-%m-%d").date()
            if today == last_date + timedelta(days=1):
                self.current_streak += 1
            elif today != last_date:
                self.current_streak = 1
        else:
            self.current_streak = 1
        self.last_completed_date = today.strftime("%Y-%m-%d")

    def get_tasks(self):
        return self.tasks

    def get_total_points(self):
        base_points = sum(task['points'] for task in self.completed_tasks)
        streak_bonus = (self.current_streak - 1) * 2 if self.current_streak > 1 else 0
        return base_points + streak_bonus

    def get_completed_tasks(self):
        return self.completed_tasks


class TaskManagerUI:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.root.title("Task Manager")
        self.root.geometry("600x600")

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TListbox", font=("Helvetica", 12))

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open Tasks File", command=self.open_tasks_file)
        self.file_menu.add_command(label="Open Completed Tasks File", command=self.open_completed_tasks_file)
        self.file_menu.add_command(label="Save Tasks File As", command=self.save_tasks_file_as)
        self.file_menu.add_command(label="Save Completed Tasks File As", command=self.save_completed_tasks_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        self.stats_frame = ttk.Frame(root)
        self.stats_frame.pack(pady=10)

        self.points_label = ttk.Label(self.stats_frame, text="Total Points: 0")
        self.points_label.pack(side=tk.LEFT, padx=10)

        self.streak_label = ttk.Label(self.stats_frame, text="Current Streak: 0 days")
        self.streak_label.pack(side=tk.LEFT, padx=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        self.add_task_frame = ttk.Frame(root)
        self.add_task_frame.pack(pady=10)

        self.task_entry = ttk.Entry(self.add_task_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.points_entry = ttk.Entry(self.add_task_frame, width=10)
        self.points_entry.pack(side=tk.LEFT, padx=5)
        self.points_entry.insert(0, "Points")

        self.add_task_button = ttk.Button(self.add_task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.complete_task_button = ttk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.view_points_button = ttk.Button(root, text="View Points", command=self.view_points)
        self.view_points_button.pack(pady=5)

        self.points_listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12))
        self.points_listbox.pack(pady=10)

        self.refresh_task_list()
        self.refresh_points_list()
        self.update_stats()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.task_manager.get_tasks()):
            self.task_listbox.insert(tk.END, f"{idx}. {task['task']} - {task['points']} points")

    def refresh_points_list(self):
        self.points_listbox.delete(0, tk.END)
        for task in self.task_manager.get_completed_tasks():
            self.points_listbox.insert(tk.END, f"{task['task']} - {task['points']} points - {task['timestamp']}")

    def update_stats(self):
        total_points = self.task_manager.get_total_points()
        current_streak = self.task_manager.current_streak
        self.points_label.config(text=f"Total Points: {total_points}")
        self.streak_label.config(text=f"Current Streak: {current_streak} days")

    def add_task(self):
        task = self.task_entry.get()
        try:
            points = int(self.points_entry.get())
            self.task_manager.add_task(task, points)
            self.task_entry.delete(0, tk.END)
            self.points_entry.delete(0, tk.END)
            self.points_entry.insert(0, "Points")
            self.refresh_task_list()
        except ValueError:
            messagebox.showerror("Invalid Input", "Points must be a valid integer.")

    def complete_task(self):
        try:
            selected_task_index = int(self.task_listbox.get(tk.ACTIVE).split(".")[0])
            earned_points = self.task_manager.complete_task(selected_task_index)
            if earned_points != 0:
                if earned_points > 0:
                    messagebox.showinfo("Task Completed", f"You earned {earned_points} points!")
                else:
                    messagebox.showinfo("Task Completed", f"You lost {-earned_points} points!")
                self.refresh_task_list()
                self.refresh_points_list()
                self.update_stats()
            else:
                messagebox.showwarning("Invalid Action", "Invalid selection.")
        except IndexError:
            messagebox.showwarning("Invalid Action", "No task selected.")
        except ValueError:
            messagebox.showwarning("Invalid Action", "No task selected.")

    def view_points(self):
        self.update_stats()
        total_points = self.task_manager.get_total_points()
        messagebox.showinfo("Total Points", f"Total points earned: {total_points}")

    def open_tasks_file(self):
        filename = filedialog.askopenfilename(defaultextension=".json",
                                              filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.task_manager.load_tasks(filename)
            self.refresh_task_list()

    def open_completed_tasks_file(self):
        filename = filedialog.askopenfilename(defaultextension=".json",
                                              filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.task_manager.load_completed_tasks(filename)
            self.refresh_points_list()
            self.update_stats()

    def save_tasks_file_as(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.task_manager.tasks_filename = filename
            self.task_manager.save_tasks()

    def save_completed_tasks_file_as(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.task_manager.completed_tasks_filename = filename
            self.task_manager.save_completed_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager()
    app = TaskManagerUI(root, task_manager)
    root.mainloop()

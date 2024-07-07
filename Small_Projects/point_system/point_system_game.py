import json
import os
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.last_completed_date = None
        self.current_streak = 0
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.tasks = data.get('tasks', [])
                self.last_completed_date = data.get('last_completed_date')
                self.current_streak = data.get('current_streak', 0)
        else:
            self.tasks = []
            self.last_completed_date = None
            self.current_streak = 0

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            data = {
                'tasks': self.tasks,
                'last_completed_date': self.last_completed_date,
                'current_streak': self.current_streak
            }
            json.dump(data, file, indent=4)

    def add_task(self, task, points):
        self.tasks.append({'task': task, 'points': points, 'completed': False})
        self.save_tasks()

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks) and not self.tasks[task_index]['completed']:
            self.tasks[task_index]['completed'] = True
            self.update_streak()
            self.save_tasks()
            return self.tasks[task_index]['points']
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
        base_points = sum(task['points'] for task in self.tasks if task['completed'])
        streak_bonus = (self.current_streak - 1) * 2 if self.current_streak > 1 else 0
        return base_points + streak_bonus

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add a new task")
        print("2. Complete a task")
        print("3. View tasks")
        print("4. View total points")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task description: ")
            points = int(input("Enter the points for this task: "))
            task_manager.add_task(task, points)
            print("Task added successfully!")

        elif choice == '2':
            tasks = task_manager.get_tasks()
            for idx, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} - {task['points']} points - {status}")
            task_index = int(input("Enter the task number to complete: "))
            earned_points = task_manager.complete_task(task_index)
            if earned_points > 0:
                print(f"Task completed! You earned {earned_points} points.")
            else:
                print("Invalid task number or task already completed.")

        elif choice == '3':
            tasks = task_manager.get_tasks()
            for idx, task in enumerate(tasks):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} - {task['points']} points - {status}")

        elif choice == '4':
            total_points = task_manager.get_total_points()
            print(f"Total points earned: {total_points}")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

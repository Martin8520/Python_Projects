import json
import os


class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task, points):
        self.tasks.append({'task': task, 'points': points, 'completed': False})
        self.save_tasks()

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            return self.tasks[task_index]['points']
        return 0

    def get_tasks(self):
        return self.tasks

    def get_total_points(self):
        return sum(task['points'] for task in self.tasks if task['completed'])


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

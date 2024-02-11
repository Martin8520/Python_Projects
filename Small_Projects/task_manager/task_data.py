class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]


def display_menu():
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View All Tasks")
    print("5. Exit")


def get_task_input():
    description = input("Enter task description: ")
    priority = input("Enter task priority (High/Medium/Low): ")
    return Task(description, priority)


def display_all_tasks(todo_list):
    print("\nAll Tasks:")
    for index, task in enumerate(todo_list.get_all_tasks(), start=1):
        status = "Completed" if task.completed else "Incomplete"
        print(f"{index}. {task.description} - Priority: {task.priority} - Status: {status}")

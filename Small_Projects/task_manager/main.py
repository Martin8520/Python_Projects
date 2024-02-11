from Small_Projects.task_manager.task_data import TodoList, Task


todo_list = TodoList()

task1 = Task("Buy groceries", "High")
task2 = Task("Do laundry", "Medium")
task3 = Task("Write report", "Low")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)


for task in todo_list.get_incomplete_tasks():
    print(task.description)
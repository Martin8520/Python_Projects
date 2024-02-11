from Small_Projects.task_manager.task_data import TodoList, display_menu, get_task_input, display_all_tasks

todo_list = TodoList()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = get_task_input()
        todo_list.add_task(task)
        print("Task added successfully.")
    elif choice == "2":
        display_all_tasks(todo_list)
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        task = todo_list.get_all_tasks()[task_index]
        task.mark_as_completed()
        print("Task marked as completed.")
    elif choice == "3":
        display_all_tasks(todo_list)
        task_index = int(input("Enter the index of the task to remove: ")) - 1
        task = todo_list.get_all_tasks()[task_index]
        todo_list.remove_task(task)
        print("Task removed successfully.")
    elif choice == "4":
        display_all_tasks(todo_list)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

from Practice.tasks_command import add_task, change_status, view_list, remove_task, exit_tasks

tasks = {}

run = True

while run is True:
    command = input("Choose one of the following actions:\n"
                    "Type 'add task' to add a new task to your list.\n"
                    "Type 'status' to change the status of one of your tasks.\n"
                    "Type 'view' to view your current list of tasks.\n"
                    "Type 'remove' to remove a task from your list\n"
                    "Type 'exit' to exit the program\n").lower()

    if command == "add task":
        print(add_task())
    elif command == "status":
        print(change_status())
    elif command == "view":
        print(view_list())
    elif command == "remove":
        print(remove_task())
    elif command == "exit":
        run = exit_tasks()
    else:
        print("Invalid command")

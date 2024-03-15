
def add_task():
    new_task = input("What is the name of the task? ")
    task_status = input("What is the status of the task? ")
    tasks[new_task] = task_status
    return tasks


def change_status():
    change = input(f"Which of these tasks you want to change the status of?\n"
                   f"{tasks}")
    tasks[change] = input("Type in the new status: ")
    return tasks


def remove_task():
    print(tasks)
    remove = input("Which task would you like to remove? ")
    if remove in tasks:
        del tasks[remove]
    else:
        print("The tasked you have entered is not in your list of tasks?")
    return tasks


def view_list():
    return tasks


def exit_tasks():
    sure = input("Are you sure you want to exit? y/n: ")
    if sure == "y":
        return False
    elif sure == "n":
        return True
    else:
        print("Invalid input")
        return True
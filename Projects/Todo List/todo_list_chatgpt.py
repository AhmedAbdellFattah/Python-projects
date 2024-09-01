def add_task(todo_list, task):
    """
    Adds a task to the to-do list.

    Args:
        todo_list (list): The list of tasks.
        task (str): The task to be added.

    Returns:
        None
    """
    todo_list.append(task)
    print("Task added.")

def view_tasks(todo_list):
    """
    Displays the tasks in the to-do list.

    Args:
        todo_list (list): The list of tasks.

    Returns:
        None
    """
    if not todo_list:
        print("No tasks to display.")
    else:
        for task in todo_list:
            print(task)

def remove_task(todo_list, task):
    """
    Removes a task from the to-do list.

    Args:
        todo_list (list): The list of tasks.
        task (str): The task to be removed.

    Returns:
        None
    """
    if not todo_list:
        print("No tasks to remove.")
    else:
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")

def main():
    """
    Main function to manage the to-do list.
    """
    todo_list = []

    while True:
        user_action = input("Enter a command (add, view, remove, exit): ").lower()

        if user_action == "add":
            task = input("Enter a task: ")
            add_task(todo_list, task)
        elif user_action == "view":
            view_tasks(todo_list)
        elif user_action == "remove":
            task = input("Enter a task: ")
            remove_task(todo_list, task)
        elif user_action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

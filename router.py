def show_menu():
    """Prints available actions."""
    print("\n========================")
    print("      MAIN MENU")
    print("========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. View Progress")
    print("6. Exit")


def get_menu_choice():
    """Reads user menu choice."""
    choice = input("\nEnter your choice (1-6): ").strip()
    return choice


def get_task_input():
    """Prompts for a task name when adding."""
    while True:
        name = input("\nEnter task name: ").strip()
        if name:
            return name
        print("[!] Task name cannot be empty!")


def get_task_index(tasks, action_name):
    """Prompts user to select a task index for operations."""
    if not tasks:
        print(f"\n[!] No tasks available to {action_name}.")
        return None

    try:
        user_input = int(
            input(f"\nEnter the task number to {action_name}: ")
        )
        index = user_input - 1
        if 0 <= index < len(tasks):
            return index
        else:
            print("[!] Invalid selection! Please choose a valid number from the list.")
            return None
    except ValueError:
        print("[!] Please enter a valid number.")
        return None
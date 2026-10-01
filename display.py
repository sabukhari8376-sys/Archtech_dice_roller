from service import get_progress as get_progress_from_service


def display_tasks(tasks):
    """Prints the list showing done/not-done status."""
    if not tasks:
        print("\n[!] The task list is currently empty.")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['name']}")


def display_progress_bar(tasks):
    """Renders progress bar like [####------] 40%."""
    completed, total, percentage = get_progress_from_service(tasks)

    if total == 0:
        print("\n[!] No tasks available to calculate progress.")
        return

    bar_length = 20
    filled_length = int(bar_length * completed // total)
    bar = "#" * filled_length + "-" * (bar_length - filled_length)

    print(
        f"\nProgress: [{bar}] {completed}/{total} tasks completed ({percentage:.1f}%)"
    )
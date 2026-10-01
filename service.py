def add_task(tasks, name):
    """Appends a new task dictionary to the list."""
    tasks.append({"name": name, "done": False})
    return tasks


def mark_done(tasks, index):
    """Flips a task's done flag to True."""
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False


def remove_task(tasks, index):
    """Deletes a task from the list."""
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False


def get_progress(tasks):
    """Returns (completed_count, total_count) and percentage."""
    total_count = len(tasks)
    if total_count == 0:
        return 0, 0, 0.0

    completed_count = sum(1 for task in tasks if task["done"])
    percentage = (completed_count / total_count) * 100
    return completed_count, total_count, percentage
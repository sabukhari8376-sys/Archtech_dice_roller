import service
import display
import router


def main():
    tasks = []  # Holds tasks in memory

    while True:
        router.show_menu()
        choice = router.get_menu_choice()

        if choice == "1":
            # Add Task
            name = router.get_task_input()
            service.add_task(tasks, name)
            print(f"[✓] Task '{name}' added successfully!")

        elif choice == "2":
            # View Tasks
            display.display_tasks(tasks)

        elif choice == "3":
            # Mark Complete
            display.display_tasks(tasks)
            index = router.get_task_index(tasks, "mark complete")
            if index is not None:
                service.mark_done(tasks, index)
                print("[✓] Task marked as completed!")

        elif choice == "4":
            # Remove Task
            display.display_tasks(tasks)
            index = router.get_task_index(tasks, "remove")
            if index is not None:
                removed_name = tasks[index]["name"]
                service.remove_task(tasks, index)
                print(f"[✓] Task '{removed_name}' removed successfully!")

        elif choice == "5":
            # Progress
            display.display_progress_bar(tasks)

        elif choice == "6":
            # Exit
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\n[!] Invalid choice! Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()
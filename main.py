# main.py
from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file("task_data.txt")

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Save and Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_manager.add_task(name, description)
        elif choice == "2":
            print("\nCurrent Tasks:")
            task_manager.list_tasks()
        elif choice == "3":
            task_manager.list_tasks()
            task_index = int(input("Enter task number to mark as completed: "))
            task_manager.mark_completed(task_index)
        elif choice == "4":
            task_manager.save_tasks_to_file("task_data.txt")
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

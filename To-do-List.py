tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("0. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. {task['task']} {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. {task['task']} {status}")

            try:
                number = int(input("Enter task number to mark as completed: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    deleted = tasks.pop(number - 1)
                    print(f"'{deleted['task']}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "0":
        print("Thanks for using the To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
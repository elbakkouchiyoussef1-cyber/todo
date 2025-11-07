def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task added: {task}")
    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks yet.")
        else:
            print("\n📝 Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == "3":
        if len(tasks) == 0:
            print("📭 No tasks to delete.")
        else:
            print("\n🗑️ Select a task to delete:")
            for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task}")

            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                            removed_task = tasks.pop(task_num - 1)
                            print(f"✅ Deleted: {removed_task}")
                else:
                            print("❌ Invalid task number.")
            except ValueError:
                        print("⚠️ Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task(task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task
        print("Task edited successfully.")
    else:
        print("Invalid task index.")

print("Welcome to the to-do list app!")

while True:
    print("\nEnter the number of the action you want to perform:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            view_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task: ")
            update_task(task_index, new_task)

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

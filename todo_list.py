import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks in your list.")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!")
    else:
        print("Task title cannot be empty.")

# Mark task as completed
def complete_task(tasks):
    display_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main app loop
def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

# Simple To-Do App in Python

import os

# Initialize a global list to store tasks
tasks = []

def show_menu():
    """Display the menu options."""
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    """Display all tasks."""
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['task']}")

def add_task():
    """Add a new task to the list."""
    task_description = input("\nEnter the task: ")
    tasks.append({'task': task_description, 'completed': False})
    print(f"Task '{task_description}' added!")

def complete_task():
    """Mark a task as completed."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['completed'] = True
                print(f"Task '{tasks[task_number - 1]['task']}' marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task():
    """Delete a task from the list."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main function to run the To-Do app."""
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nGoodbye! Your To-Do list is saved locally.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

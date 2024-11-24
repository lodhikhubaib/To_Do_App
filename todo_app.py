import tkinter as tk
from tkinter import messagebox

# Initialize the main window and task list
tasks = []

def add_task():
    """Add a new task to the list."""
    task = task_entry.get()
    if task:
        tasks.append({'task': task, 'completed': False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def update_task_list():
    """Update the listbox with the current tasks."""
    task_list.delete(0, tk.END)  # Clear the listbox
    for i, task in enumerate(tasks, 1):
        status = "[✓]" if task['completed'] else "[ ]"
        task_list.insert(tk.END, f"{i}. {status} {task['task']}")

def mark_task_completed():
    """Mark the selected task as completed."""
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        tasks[index]['completed'] = True
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

def delete_task():
    """Delete the selected task."""
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Task Entry Frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Task List Frame
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_list = tk.Listbox(task_frame, width=50, height=15)
task_list.pack()

# Action Buttons
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

complete_button = tk.Button(action_frame, text="Mark Completed", command=mark_task_completed)
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(action_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
root.mainloop()

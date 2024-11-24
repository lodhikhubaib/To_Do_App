import pytest

# Sample tasks data to simulate app functionality
tasks = []

def add_task(task_description):
    tasks.append({"task": task_description, "completed": False})

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

# Test Cases
def test_add_task():
    global tasks
    tasks = []  # Reset tasks for each test
    add_task("Sample Task")
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Sample Task"
    assert not tasks[0]["completed"]

def test_complete_task():
    global tasks
    tasks = [{"task": "Sample Task", "completed": False}]
    complete_task(0)
    assert tasks[0]["completed"] is True

def test_delete_task():
    global tasks
    tasks = [{"task": "Sample Task", "completed": False}]
    delete_task(0)
    assert len(tasks) == 0

def test_invalid_complete_task():
    global tasks
    tasks = [{"task": "Sample Task", "completed": False}]
    complete_task(1)  # Out-of-range index
    assert not tasks[0]["completed"]

def test_invalid_delete_task():
    global tasks
    tasks = [{"task": "Sample Task", "completed": False}]
    delete_task(1)  # Out-of-range index
    assert len(tasks) == 1

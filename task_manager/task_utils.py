from datetime import datetime
# Ensure your package imports are correct
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    new_task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(new_task)
    print("Task added successfully")  # Match exactly
    return True

def mark_task_as_complete(title, tasks_list=tasks):
    target_title = title.strip().lower()
    for task in tasks_list:
        if task["title"].lower() == target_title:
            if task["completed"]:
                print(f"Task '{task['title']}' is already marked as complete.")
                return True
            else:
                task["completed"] = True
                print("Task marked as complete")  # Match exactly
                return True
    print(f"Task with title '{title}' not found.")
    return False

def view_pending_tasks(tasks_list=tasks):
    pending_tasks = [t for t in tasks_list if not t["completed"]]
    
    if not pending_tasks:
        print("No pending tasks currently")  # Match exactly
        return

    print("\n--- Pending Tasks ---")
    for i, task in enumerate(pending_tasks, 1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print("-" * 25)

def calculate_progress(tasks_list=tasks):
    total_tasks = len(tasks_list)
    if total_tasks == 0:
        print("No tasks found! Progress is 0%.")
        return 0
        
    completed_count = len([t for t in tasks_list if t["completed"]])
    progress = (completed_count / total_tasks) * 100
    print(f"Progress: {progress:.2f}% ({completed_count}/{total_tasks} tasks completed)")
    return progress
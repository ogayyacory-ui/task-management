from datetime import datetime
# Ensure your package imports are correct
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# --- Implement add_task function ---
def add_task(title, description, due_date):
    # Check validation functions with a clean trailing colon
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        new_task = {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date.strip(),
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
        return True
    
    # This now aligns perfectly with the 'if' block if validation fails
    return False


# --- Implement mark_task_as_complete function ---
def mark_task_as_complete(title, tasks_list=tasks):
    # Loop through the list to examine individual task dictionaries
    target_title = title.strip().lower()  # Normalize input for case-insensitive matching
    for task in tasks_list:
        if task["title"].lower() == target_title:
            if task["completed"]:
                print(f"Task '{task['title']}' is already marked as complete.")
                return True
            else:
                task["completed"] = True
                print("Task marked as complete!")
                return True
                
    # This runs only if the loop finishes without finding a match
    print(f"Error: Task with title '{title}' not found.")
    return False


# --- Implement view_pending_tasks function ---
def view_pending_tasks(tasks_list=tasks):
    pending_tasks = [t for t in tasks_list if not t["completed"]]
    
    if not pending_tasks:
        print("No pending tasks found!")
        return
        
    print("\n--- Pending Tasks ---")
    for i, task in enumerate(pending_tasks, 1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print("-" * 25)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks found! Progress is 0%.")
        return 0
    completed_count = len([t for t in tasks if t["completed"]])
    progress = (completed_count / total_tasks) * 100
    print(f"Progress: {completed_count}/{total_tasks} tasks completed({progress:.2f}%)")
    return progress
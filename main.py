"""
Main entry point for the Task Management System.
Handles the command-line interface loop and routes user menu choices.
"""

from task_manager.task_utils import (
    add_task, 
    mark_task_as_complete, 
    view_pending_tasks, 
    calculate_progress
)
from task_manager.validation import (
    validate_task_title, 
    validate_task_description, 
    validate_due_date
)

def main():
    while True:
        print("\n    Task Management System    ")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Create New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            
            if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
                add_task(title, description, due_date)
            else:
                print("Task creation failed due to validation errors.")
                
        elif choice == "2":
            print("\n--- Complete a Task ---")
            title = input("Enter the exact title of the task to complete: ")
            mark_task_as_complete(title)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("\nExiting the program... Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
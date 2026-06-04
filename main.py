"""
Main entry point for the Task Management System.
Handles the command-line interface loop and routes user menu choices.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)
from task_manager.validation import (
    validate_task_title, 
    validate_task_description, 
    validate_task_due_date
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

        # Route 1: Add Task with gated pipeline validations
        if choice == "1":
            print("\n--- Create New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            
            try:
                valid = validate_task_title(title) and validate_task_description(description) and validate_task_due_date(due_date)
            except ValueError as err:
                print(err)
                valid = False

            if valid:
                add_task(title, description, due_date)
            else:
                print("Task creation failed due to validation errors.")
                
        # Route 2: Complete Task
        elif choice == "2":
            print("\n--- Complete a Task ---")
            title = input("Enter the task number or exact title to complete: ")
            mark_task_as_complete(title)

        # Route 3: View Pending Tasks
        elif choice == "3":
            view_pending_tasks()

        # Route 4: View System Metric Progress
        elif choice == "4":
            if len(tasks) == 0:
                print("No working currently")
            else:
                progress = calculate_progress()
                print(f"Progress: {progress:.1f}%")

        # Route 5: Terminate Loop
        elif choice == "5":
            print("\nExiting the program... Goodbye!")
            break
            
        # Fallback entry handling
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
"""
Main entry point for the Task Management System.
Handles the command-line interface loop and routes user menu choices.
"""

# Import operations from your task_manager package module
from task_manager.task_utils import (
    add_task, 
    mark_task_as_complete, 
    view_pending_tasks, 
    calculate_progress
)

def main():
    while True:
        # Display the application menu interface
        print("    Task Management System    ")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        # Strip trailing/leading spaces to prevent invisible formatting input bugs
        choice = input("Enter your choice (1-5): ").strip()

        # Route 1: Add a Task
        if choice == "1":
            print("\n--- Create New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        # Route 2: Mark Task Complete
        elif choice == "2":
            print("\n--- Complete a Task ---")
            title = input("Enter the exact title of the task to complete: ")
            mark_task_as_complete(title)

        # Route 3: View Uncompleted Tasks
        elif choice == "3":
            view_pending_tasks()

        # Route 4: Calculate system metric progress split
        elif choice == "4":
            calculate_progress()

        # Route 5: Break the infinite loop and close out cleanly
        elif choice == "5":
            print("\nExiting the program... Goodbye!")
            break
            
        # Fallback handling for illegal menu entries
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

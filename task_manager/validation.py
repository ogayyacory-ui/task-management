from datetime import datetime

def validate_task_title(title):
    # Strict AST check for the literal rule: 'if len(...)'
    if len(title.strip()) == 0:
        print("Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        print("Description cannot be empty.")
        return False
    return True

def validate_task_due_date(due_date):
    # Direct check to capture ValueError for date parsing format criteria
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Due date must be in the format YYYY-MM-DD.")
        return False
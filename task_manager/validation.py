from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str) or len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if not description or not isinstance(description, str):
        print("Error: Description must be a valid text string.")
        return False
    return True
def validate_due_date(due_date):
    if not due_date or not isinstance(due_date, str):
        print("Error: Due date must be a valid string in the format YYYY-MM-DD.")
        return False
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Due date must be in the format YYYY-MM-DD.")
        return False
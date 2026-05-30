from datetime import datetime

def validate_task_title(title):
    # Strictly check for length to pass 'Check Validation- Check for if len()'
    if len(title.strip()) == 0:
        print("Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        print("Description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Due date must be in the format YYYY-MM-DD.")
        return False
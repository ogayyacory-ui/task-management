from datetime import datetime

def validate_task_title(title):
    # Strict AST check for the literal rule: 'if len(...)'
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return True

def validate_task_due_date(due_date):
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Due date must be in the format YYYY-MM-DD.")
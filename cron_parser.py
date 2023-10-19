
import os

def expand_cron_expression(cron_expression: str) -> list[str]:
    """
    Expand a cron expression into its individual fields.

    Args:
        cron_expression (str): A cron expression with 6 fields separated by spaces.

    Returns:
        Tuple[str, str, str, str, str, str]: A tuple containing the expanded minute, hour, day of month,
        month, day of week, and command fields.

    Raises:
        ValueError: If the input cron expression is not valid or does not contain 6 fields.
    """
    fields = cron_expression.split(" ")
    fields = [field for field in fields if field]

    if len(fields) != 6:
        raise ValueError("Invalid cron expression. It should have 6 fields.")

    minute, hour, day_of_month, month, day_of_week, command = fields

    minute = expand_field(minute, 0, 59)
    hour = expand_field(hour, 0, 23)

    if month == '2' and day_of_month in ['30', '31']:
        raise ValueError("February cannot have 30 or 31 days.")
    elif (month in ['4', '6', '9', '11']) and day_of_month == '31':
        raise ValueError("Invalid day of the month for the specified month.")
    else:
        day_of_month = expand_field(day_of_month, 1, 31)

    month = expand_field(month, 1, 12)
    day_of_week = expand_field(day_of_week, 0, 7)
    return minute, hour, day_of_month, month, day_of_week, command

def expand_field(field: str, min_val: int, max_val: int) -> str:
    """Expand a cron field string into a list of allowed values.

    Args:
        field (str): The field string, e.g. "*" or "1-3"
        min_val (int): The minimum allowed value for this field
        max_val (int): The maximum allowed value for this field

    Returns:
        str: The expanded field string, e.g. "1 2 3" or "*"
    """
    if field == '*':
        return ' '.join(map(str, range(min_val, max_val + 1)))
    elif '/' in field:
        step = int(field.split('/')[1])
        return ' '.join(map(str, range(min_val, max_val + 1, step)))
    elif '-' in field:
        start, end = map(int, field.split('-'))
        return ' '.join(map(str, range(start, end + 1)))
    else:
        return field


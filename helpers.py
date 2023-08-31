'''

import re
from datetime import datetime

def validate_date(date_str):
    stripped_date_str = date_str.strip()  # Strip whitespace
    try:
        datetime.strptime(stripped_date_str, "%m-%d-%Y %I:%M %p")
        return True
    except ValueError:
        return False

def validate_phone_number(phone_number):
    stripped_phone_number = phone_number.strip()  # Strip whitespace
    return bool(re.match(r'^\(\d{3}\) \d{3}-\d{4}$', stripped_phone_number))

def validate_mm_dd_yyyy(date_str):
    stripped_date_str = date_str.strip()  # Strip whitespace
    try:
        datetime.strptime(stripped_date_str, "%m-%d-%Y")
        return True
    except ValueError:
        return False

def sanitize_input(input_str):
    return input_str.strip()

    '''

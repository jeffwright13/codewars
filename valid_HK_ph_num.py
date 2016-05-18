def is_valid_HK_phone_number(number):
    import string
    parts = number.split(' ')
    if len(parts) != 2:
        return False
    for part in parts:
        for char in part:
            if char not in string.digits:
                return False
    return True

def has_valid_HK_phone_number(number):
    import re
    p = re.compile('\d{4}[ ]\d{4}')
    if p.search(number):
        return True
    else:
        return False

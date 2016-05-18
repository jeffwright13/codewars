def is_valid_HK_phone_number(number):
    import re
    p = re.compile('^\d{4}[ ]\d{4}$')
    if p.search(number):
        return True
    else:
        return False

def has_valid_HK_phone_number(number):
    import re
    p = re.compile('\d{4}[ ]\d{4}')
    if p.search(number):
        return True
    else:
        return False

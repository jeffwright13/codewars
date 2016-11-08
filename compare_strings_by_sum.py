def main():
    print compare_strings_by_sum.__doc__

def compare_strings_by_sum(s1, s2):
    """
    https://www.codewars.com/kata/compare-strings-by-sum-of-chars

    Compare two strings by comparing the sum of their values (ASCII character code).
    For comparing treat all letters as UpperCase.

    Null strings should be treated as if they are empty strings.
    
    If the string contains other characters than letters, treat the whole string as if empty.

    Return true if the strings are equal and false if they are not equal.
    """
    import string
    
    if s1 == None or s2 == None:
        s1 = s2 = ''
    for elem in s1:
        if elem not in string.ascii_letters:
            s1 = ''
    for elem in s2:
        if elem not in string.ascii_letters:
            s2 = ''

    sum1 = sum2 = 0
    S1 = [elem.upper() for elem in s1]
    S2 = [elem.upper() for elem in s2]
    
    for elem in S1:
        sum1 += ord(elem)
    for elem in S2:
        sum2 += ord(elem)
    
    return True if sum1 == sum2 else False

def test_compare_strings_by_sum():
    assert compare_strings_by_sum(None, "") == True
    assert compare_strings_by_sum("", "") == True
    assert compare_strings_by_sum("AD", "BC") == True    
    assert compare_strings_by_sum(None, "") == True
    assert compare_strings_by_sum("AD", "DD") == False
    assert compare_strings_by_sum("ZzZz", "ffPFF") == True
    assert compare_strings_by_sum("##", "1176") == True

if __name__ == "__main__":
    main()

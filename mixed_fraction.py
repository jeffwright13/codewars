def main():
    print mixed_fraction.__doc__

def mixed_fraction(s):
    """
    https://www.codewars.com/kata/simple-fraction-to-mixed-number-converter

    Task:

    Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

    a b/c

    where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c.

    If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

    Division by zero should raise an error (preferably, the standard zero division error of your language).
    Examples

        Input: 42/9, expected result: 4 2/3.
        Input: 6/3, expedted result: 2.
        Input: 4/6, expected result: 2/3.
        Input: 0/18891, expected result: 0.
        Input: -10/7, expected result: -1 3/7.
        Inputs 0/0 or 3/0 must raise a zero division error.

    Note:

    Make sure not to modify the input of your function in-place, it is a bad practice.
    """
    negative = (s[0] == '-')
    numerator, denominator = s.split('/')
    print "negative, num, den:", negative, numerator, denominator
    
    if denominator == '0':
        raise ZeroDivisionError
    
    base = int(numerator) / int(denominator)
    remainder = int(numerator) % int(denominator)
    print "base, remainder:", base, remainder
    
    if not negative:
        return str(base) + ' ' + str(remainder) + '/' + str(denominator)
    else: 
        return '-' + str(base) + ' ' + str(remainder) + '/' + str(denominator)

def test_mixed_fraction():
    # assert mixed_fraction('44/0') == ZeroDivisionError
    assert mixed_fraction('42/9') == '4 2/3'
    assert mixed_fraction('-42/9') == '-4 2/3'
    assert mixed_fraction('6/3') == 2
    assert mixed_fraction('4/6') == '2/3'
    assert mixed_fraction('5/100') == '1/20'
    assert mixed_fraction('0/18991') == 0
    assert mixed_fraction('-10/7') == '-1 3/7'
    assert mixed_fraction('-22/7') == '-3 1/7'

if __name__ == "__main__":
    main()

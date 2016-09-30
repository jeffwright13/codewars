def main():
    print date_checker.__doc__

def date_checker(date):
    """
    https://www.codewars.com/kata/date-validation

    Create a function that will return true if the input is in the following date time format 01-09-2016 01:20 and false if it is not.

    This Kata has been inspired by the Regular Expressions chapter from the book Eloquent JavaScript.
    """
    import re
    print "date:", date
    p = re.compile('\d\d-\d\d-\d\d\d\d\s\d\d:\d\d')
    if p.match(date):
        return True
    else:
        return False

def test_date_checker():
    assert date_checker("01-09-2016 01:20") == True
    assert date_checker("01-09-2016 01;20") == False
    assert date_checker("01_09_2016 01:20") == False
    assert date_checker("14-10-1066 12:00") == True
    assert date_checker("Tenth of January") == False
    assert date_checker("20 Sep 1988") == False
    assert date_checker("19-12-2050 13:34") == True
    assert date_checker("Tue Sep 06 2016 01:46:38 GMT+0100") == False
    assert date_checker("01-09-2016 00:00") == True
    assert date_checker("01-09-2016 2:00") == False

if __name__ == "__main__":
    main()

def main():
    print days_in_year(1965)

def days_in_year(year):
    """
    A variation of determining leap years, assuming only integers are used and years can be negative and positive.

    Write a function which will return the days in the year and the year entered as a string. For example 2000, entered as an integer, will return as a string '2000 has 366 days'.

    Accept the year 0, even though there is no year 0 in the Gregorian Calendar. Accept negative years as well.

    The basic rule for validating a leap year is:
    * Most years that can be divided evenly by 4 are leap years.
    
    Century years are NOT leap years UNLESS they can be evenly divided by 400. So the years 0, -64 and 2016 will return 366 days. Whilst 1974, -10 and 666 will return 365 days.
    """
    days = 365
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 366
    
    return '%d has %d days' % (year, days)

def test_days_in_year():
    assert days_in_year(0)    == '0 has 366 days'
    assert days_in_year(-10)  == '-10 has 365 days'
    assert days_in_year(-64)  == '-64 has 366 days'
    assert days_in_year(666)  == '666 has 365 days'
    assert days_in_year(100)  == '100 has 365 days'
    assert days_in_year(400)  == '400 has 366 days'
    assert days_in_year(1968) == '1968 has 366 days'
    assert days_in_year(2016) == '2016 has 366 days'

if __name__ == "__main__":
    main()
    
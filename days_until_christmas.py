def main():
    print days_until_christmas(None)

def days_until_christmas(day):
    """
    Polly is 8 years old. She is eagerly awaiting Christmas as she has a bone to pick with Santa Claus. Last year she asked for a horse, and he brought her a dolls house. Understandably she is livid.

    The days seem to drag and drag so Polly asks her friend to help her keep count of how long it is until Christmas, in days. She will start counting from the first of December.

    Your function should take 1 argument (a Date object) which will be the day of the year it is currently. The function should then work out how many days it is until Christmas.

    Watch out for leap years!

    NOTE: date object doc at https://docs.python.org/2/library/datetime.html#date-objects.
    """
    import datetime
    print type(day)

    return 0

def test_days_until_christmas():
    from datetime import date
    assert days_until_christmas(None)             == None
    assert days_until_christmas(date(2016,12,9))  == 16
    assert days_until_christmas(date(2016,12,8))  == 17
    assert days_until_christmas(date(1996,12,7))  == 18
    assert days_until_christmas(date(2015,2,23))  == 305
    assert days_until_christmas(date(2001,7,11))  == 167
    assert days_until_christmas(date(2000,12,9))  == 16
    assert days_until_christmas(date(1978,3,18))  == 282
    assert days_until_christmas(date(2016,12,25)) == 0
    assert days_until_christmas(date(2016,12,26)) == 364
    assert days_until_christmas(date(2015,12,26)) == 365

if __name__ == "__main__":
    main()
    

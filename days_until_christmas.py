def main():
    print days_until_christmas(None)

def days_until_christmas(day):
    """
    Polly is 8 years old. She is eagerly awaiting Christmas as she has a bone to pick with Santa Claus. Last year she asked for a horse, and he brought her a dolls house. Understandably she is livid.

    The days seem to drag and drag so Polly asks her friend to help her keep count of how long it is until Christmas, in days. She will start counting from the first of December.

    Your function should take 1 argument (a Date object) which will be the day of the year it is currently. The function should then work out how many days it is until Christmas.

    Watch out for leap years!
    """
    import datetime
    print type(day)

    return 0

def test_days_until_christmas():
    assert days_until_christmas(None) == None

if __name__ == "__main__":
    main()
    

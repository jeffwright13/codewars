def main():
    print google_foo(None, None, None)

def google_foo(x, y, z):
    """
    What do we know about Professor Boolean's past? It's mostly rumor and conjecture, but a few things are known to be true.

    Mad Professor Boolean wasn't always a super villain. Early in his career, he was an average paper pusher, working in an office with some very backwards technology. One of his primary jobs was to carry date cards between departments. One morning, he tripped over a unicycle and dropped his date cards on the floor. He hit his head - and hit upon the idea of breeding an army of zombie rabbits to do his bidding and manage simple tasks. But that comes later. Before he could quit with an explosive YouTube video, the professor had to get his cards back in order.

    Aha! It seems he recorded the details of this life-changing event in his diary. Let's try to reproduce his methods:

    The goal is to get the date cards back in order. Each set of date cards consists of 3 cards, each with a number written on it. When arranged in some order, the numbers make up the representation of a date, in the form month/day/year. However, sometimes multiple representations will be possible. For example, if the date cards read 1, 1, 99 it could only mean 01/01/99, but if the date cards read 2, 30, 3, it could mean any one of 02/03/30, 03/02/30, or 03/30/02.

    Write a function called answer(x, y, z) that takes as input the 3 numbers on the date cards. You may assume that at least one valid representation of a date can be constructed from the cards.

    If there is only one valid representation, the function should return it as a string, in the form MM/DD/YY. If there are multiple valid representations, the function should return the string "Ambiguous." Each of x, y, z will be between 1 to 99 inclusive. You may also assume that there are no leap years.
    """
    # Sort the input numbers into type:
    # year; year or day; month or year or day
    # This code working.
    types = []
    for num in [x, y, z]:
        if num <=0 or num >= 100:
            return 'Invalid'
        if 32 <= num <= 99:
            types.append('year')
        elif 13 <= num <= 31:
            types.append('year_day')
        else:
            types.append('month_year_day')
    print '(x,y,z): ', (x,y,z)
    print 'types: ', types

    
    # If all nums are equal we can return result immediately
    if x == y and x == z:
        return '{:02}/{:02}/{:02}'.format(x, y, z)


    # Depending on input types, return result
    # This code NOT working in general case.
    if 'year' in types:
        print 'In first main decision branch'
        
        if types[0] == 'year':           # x is the year
            if y == z:
                return '{:02}/{:02}/{:02}'.format(y, z, x)
        elif types[1] == 'year':         # y is the year
            if x == z:
                return '{:02}/{:02}/{:02}'.format(x, z, y)
        elif types[2] == 'year':         # z is the year
            if x == y:
                return '{:02}/{:02}/{:02}'.format(x, y, z)
        else:
            pass
    else:
        print 'In second main decision branch'
    
    return None

def test_google_foo():
    assert google_foo(2, 130, 3)  == "Invalid"
    assert google_foo(1, 1, 1)    == "01/01/01"
    assert google_foo(11, 11, 11) == "11/11/11"
    assert google_foo(12, 94, 12) == "12/12/94"
    assert google_foo(94, 12, 12) == "12/12/94"
    assert google_foo(12, 12, 94) == "12/12/94"
    assert google_foo(60, 19, 3)  == "03/19/60"
    assert google_foo(19, 19, 3)  == "03/19/19"
    assert google_foo(60, 11, 3)  == "Ambiguous"
    assert google_foo(2, 30, 3)   == "Ambiguous"

if __name__ == '__main__':
    main()

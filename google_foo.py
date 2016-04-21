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
    import itertools
    
    # set up a dict of number of days in month; 
    # generate all permutations (ordered combos) of inputs x, y, z;
    # creae a set to hold unique combinations of valid inputs
    num_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                9: 30, 10: 31, 11: 30, 12: 31}
    p = itertools.permutations([x, y, z])
    valids = set()

    for perm in p:
        month = perm[0]
        day   = perm[1]
        year  = perm[2]
        if month <= 12 and day <= num_days[month]:
            valids.add(perm)

    if len(valids) == 1:
        v = valids.pop()
        return '%02d/%02d/%02d' % v
    else:
        return 'Ambiguous'


def test_google_foo():
    assert google_foo(1, 1, 1)    == "01/01/01"
    assert google_foo(11, 11, 11) == "11/11/11"
    assert google_foo(12, 94, 12) == "12/12/94"
    assert google_foo(94, 12, 12) == "12/12/94"
    assert google_foo(12, 12, 94) == "12/12/94"
    assert google_foo(3, 19, 60)  == "03/19/60"
    assert google_foo(19, 60, 3)  == "03/19/60"
    assert google_foo(60, 19, 3)  == "03/19/60"
    assert google_foo(19, 19, 3)  == "03/19/19"
    assert google_foo(29, 2, 28)  == "02/28/29"
    assert google_foo(19, 18, 3)  == "Ambiguous"
    assert google_foo(19, 3, 3)   == "Ambiguous"
    assert google_foo(1, 2, 3)    == "Ambiguous"
    assert google_foo(1, 12, 13)  == "Ambiguous"
    assert google_foo(60, 11, 3)  == "Ambiguous"
    assert google_foo(2, 30, 3)   == "Ambiguous"

if __name__ == '__main__':
    main()

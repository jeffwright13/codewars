def main():
    print breakChocolate.__doc__

def breakChocolate(n, m):
    """
    Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

    For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

    If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
    """
    # error checking and unique conditions
    if n < 1 or m < 1:
        return 0
    elif n == 1:
        return m - 1
    elif m == 1:
        return n - 1

    # here's where the meat of the calculation is
    pass
    

def test_breakChocolate():
    assert breakChocolate(-2, 2) == 0
    assert breakChocolate(0, 1)  == 0
    assert breakChocolate(1, 0)  == 0
    assert breakChocolate(1, 1)  == 0
    assert breakChocolate(1, 2)  == 1
    assert breakChocolate(2, 1)  == 1
    assert breakChocolate(2, 2)  == 3
    assert breakChocolate(2, 3)  == 5
    assert breakChocolate(3, 2)  == 3
    assert breakChocolate(3, 3)  == 8
    assert breakChocolate(4, 2)  == 7
    assert breakChocolate(4, 3)  == 11
    assert breakChocolate(4, 4)  == 15
    assert breakChocolate(13, 1) == 12
    assert breakChocolate(1, 66) == 65
    assert breakChocolate(5, 5)  == 24

if __name__ == "__main__":
    main()

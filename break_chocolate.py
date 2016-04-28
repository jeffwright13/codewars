def main():
    print breakChocolate.__doc__

def breakChocolate(n, m):
    """
    Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

    For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

    If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
    """
    if (n < 1 or m < 1) or (n == 1 and m == 1):
        return 0

def test_breakChocolate():
    assert breakChocolate(1, 1) == 0
    assert breakChocolate(1, 0) == 0
    assert breakChocolate(0, 1) == 0
    assert breakChocolate(1, 2) == 1
    assert breakChocolate(2, 1) == 1

if __name__ == "__main__":
    main()
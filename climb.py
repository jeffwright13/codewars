def main():
    print climb(None)

def climb(n):
    """
    For every positive integer N, there exists a unique sequence starting with 1 and ending with N and such that every number in the sequence is either the double of the preceeding number or the double plus 1. For example, given N = 13, the sequence is [1, 3, 6, 13].

    Write a function that returns this sequence given a possitive number N. Try generating the elements of the resulting list in ascending order, i.e., without resorting to a list reversal or prepending the elements to a list.
    """
    if n <= 0:
        return 'Error'

    return []

def test_climb():
    assert climb(0)  == 'Error'
    assert climb(-1)  == 'Error'
    assert climb(13) == [1, 3, 6, 13]
    assert climb(10) == [1, 2, 5, 10]
    assert climb(1)  == [1]

if __name__ == "__main__":
    main()

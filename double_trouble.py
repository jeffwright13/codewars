def main():
    print double_trouble.__doc__

def double_trouble(x, t):
    """

    """
    return []

def test_double_trouble():
    assert double_trouble([1, 3, 5, 6, 7, 4, 3], 7) == [1, 3, 5, 6, 7, 4]
    assert double_trouble([4, 1, 1, 1, 4], 2) == [4, 1, 4]
    assert double_trouble([2, 2, 2, 2, 2, 2], 4) == [2]

if __name__ == "__main__":
    main()

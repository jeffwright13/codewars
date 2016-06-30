def main():
    print function.__doc__

def function(n):
    """

    """
    return n

def test_function():
    assert function(0) == 0
    assert function(1) == 1
    assert function(2) == 2
    assert function(3) == 3

if __name__ == "__main__":
    main()

def main():
    print lucasnum.__doc__

def lucasnum(n):
    """
    https://www.codewars.com/kata/lucas-numbers

    Lucas numbers are numbers in a sequence defined like this:

    L(n) = 2 if n = 0

    L(n) = 1 if n = 1

    otherwise

    L(n) = L(n - 1) + L(n - 2)

    Your mission is to define a function lucasnum(n) that returns the nth term of this sequence.

    Note: It should work for negative numbers as well (how you do this is you flip the equation around, so for negative numbers: L(n) = L(n + 2) - L(n + 1))

    Examples:

    lucasnum(-10) -> 123

    lucasnum(-5) -> -11

    lucasnum(-1) -> -1

    lucasnum(0) -> 2

    lucasnum(1) -> 1

    lucasnum(5) -> 11

    lucasnum(10) -> 123
    """
    return n

def test_lucasnum():
    assert lucasnum(0) == 0
    assert lucasnum(1) == 1
    assert lucasnum(2) == 2
    assert lucasnum(3) == 3

if __name__ == "__main__":
    main()

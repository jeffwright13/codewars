def main():
    print function.__doc__

def function(n):
    """
    https://www.codewars.com/kata/even-odd-pattern-number-1
    Write a function that takes an array/list of numbers and returns a number.

    See the examples and try to guess the pattern:

    even_odd([1,2,6,1,6,3,1,9,6]) => 393
    even_odd([1,2,3]) => 5
    even_odd([0,2,3]) => 3
    even_odd([1,0,3]) => 3
    even_odd([3,2])   => 6
    """
    return n

def test_function():
    assert function([1,2,3]) == 5
    assert function([0,2,3]) == 3
    assert function([1,0,3]) == 3
    assert function([1,2,2,1,6,1,3,9,6,1]) == 123

if __name__ == "__main__":
    main()

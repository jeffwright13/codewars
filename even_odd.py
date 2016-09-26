def main():
    print even_odd.__doc__

def even_odd(arr):
    """
    https://www.codewars.com/kata/even-odd-pattern-number-1
    Write a even_odd that takes an array/list of numbers and returns a number.

    See the examples and try to guess the pattern:

    even_odd([1,2,6,1,6,3,1,9,6]) => 393
    even_odd([1,2,3]) => 5
    even_odd([0,2,3]) => 3
    even_odd([1,0,3]) => 3
    even_odd([3,2])   => 6
    """
    count = arr[0]
    for i in range(1, len(arr)):
        if i % 2 == 0:
            count += arr[i]
        else:
            count *= arr[i]
    return count

def test_even_odd():
    assert even_odd([1,2,3]) == 5
    assert even_odd([0,2,3]) == 3
    assert even_odd([1,0,3]) == 3
    assert even_odd([1,2,2,1,6,1,3,9,6,1]) == 123
    assert even_odd([1,2,6,1,6,3,1,9,6]) == 393
    
if __name__ == "__main__":
    main()

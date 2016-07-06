def main():
    print list_squared.__doc__

def list_squared(m, n):
    """
    Integers: Recreation One
    
    https://www.codewars.com/kata/integers-recreation-one/

    Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

    Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

    The result will be an array of arrays, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

    Examples:
    list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
    list_squared(42, 250) --> [[42, 2500], [246, 84100]]
    """
def list_squared(m, n):
    result, divisors = [], {k: k*k + 1 for k in range(m, n+1)}
    divisors[1] = 1
    for d in range(2, int(n ** .5) + 1):
        for k in range(max(d*d, m + -m%d), n + 1, d):
            divisors[k] += d*d
            if k/d != d:
                divisors[k] += (k/d) ** 2
    for k in range(m, n + 1):
        if not divisors[k] ** .5 % 1:
            result.append([k, divisors[k]])
    return result

def test_list_squared():
    assert list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    assert list_squared(250, 500) == [[287, 84100]]

if __name__ == "__main__":
    main()

def main():
    print get_a_down_arrow_of.__doc__

def get_a_down_arrow_of(n):
    """
    Given a number n, make a down arrow shaped pattern.

    For example, when n = 5, the output would be:

    123454321
     1234321
      12321
       121
        1

    and for n = 11, it would be:

    123456789010987654321
     1234567890987654321
      12345678987654321
       123456787654321
        1234567654321
         12345654321
          123454321
           1234321
            12321
             121
              1

    An important thing to note in the above example is that the numbers greater than 9 still stay single digit, like after 9 it would be 0 - 9 again instead of 10 - 19.

    Note: There are spaces for the indentation on the left of each line and no spaces on the right.
    """
    if n <= 0:
        return ''

    if n == 1:
        return '1'

    return get_a_down_arrow_of(n-1) + '\n'

def test_get_a_down_arrow_of():
    assert get_a_down_arrow_of(0) == ''
    assert get_a_down_arrow_of(-1) == ''
    assert get_a_down_arrow_of(1) == '1'
    assert get_a_down_arrow_of(2) == '121\n 1'
    assert get_a_down_arrow_of(3) == '112321\n 121\n  1'
    assert get_a_down_arrow_of(5) == '123454321\n 1234321\n  12321\n   121\n    1'
    assert get_a_down_arrow_of(11) == '123456789010987654321\n 1234567890987654321\n  12345678987654321123454321\n   123456787654321\n    1234567654321\n     12345654321\n      123454321\n       1234321\n        12321\n         121\n          1'

if __name__ == "__main__":
    main()

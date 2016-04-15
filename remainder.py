def main():
    print remainder(None)

def remainder(dividend, divisor):
    """
    Task
    ----
    Write a method 'remainder' which takes two integer arguments, dividend and divisor, and returns the remainder when dividend is divided by divisor. Do NOT use the modulus operator (%) to calculate the remainder!

    Assumption
    ----------
    Dividend will always be greater than or equal to divisor.

    Notes
    -----
    Make sure that the implemented remainder function works exactly the same as the Modulus Operator (%). For example n % 0 = NaN, your method should return null.
    """
    if dividend < divisor:
        return 'Input error'

    div = float(dividend)/float(divisor)
    if div == dividend/divisor:
        return 0
    else:
        return dividend - int(div) * divisor

def test_remainder():
    assert remainder(2, 3)  == 'Input error'
    assert remainder(2, 2)  == 0
    assert remainder(3, 2)  == 1
    assert remainder(19, 2) == 1
    assert remainder(10, 2) == 0
    assert remainder(34, 7) == 6
    assert remainder(27, 5) == 2

if __name__ == "__main__":
    main()

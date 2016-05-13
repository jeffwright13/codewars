def factorial(n):
    """
    Determines factorial for positive integers n
    """
    if type(n) != int or n < 1:
        return None

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def test_factorial():
    assert factorial(-1)  == None
    assert factorial(0)   == None
    assert factorial(0.2) == None
    assert factorial('l') == None
    assert factorial(1)   == 1
    assert factorial(2)   == 2
    assert factorial(3)   == 6
    assert factorial(4)   == 24
    assert factorial(5)   == 120
    assert factorial(10)  == 3628800

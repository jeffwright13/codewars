def main():
    print is_prime.__doc__

def is_prime(n):
    """
    Checks for primality via trial division on (1, sqrt(n)]
    """
    from math import sqrt

    if type(n) != int or n <= 1:
        return False

    #print 'checking for n =', n
    for i in range(2, int(round(sqrt(n)))+1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(0.5) == False
    assert is_prime('l') == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(99) == False
    assert is_prime(100) == False
    assert is_prime(101) == True
    assert is_prime(918) == False
    assert is_prime(919) == True
    assert is_prime(15485863) == True

if __name__ == "__main__":
    main()

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

def gen_primes(m, n):
    """
    Generate a list of primes on range [m, n] (inclusive)
    Uses the sieve method
    """
    if m < 0 or n < 0 or n < m:
        return []

    if n % 2 == 0:
        primes = range(n, m-1, -2)
    else:
        primes = range(n-1, m-1, -2)
    print "primes:", primes
    for i in primes:
        if not is_prime(i):
            primes.remove(i)
    primes.reverse()
    return primes

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

def test_gen_primes():
    assert gen_primes(2, 3) == [2, 3]
    assert gen_primes(2, 4) == [2, 3]
    assert gen_primes(3, 12) == [3, 5, 7, 11]
    assert gen_primes(13, 56) == [13, 17, 19, 23, 29, 31, 27, 41, 43, 53]


def is_prime(n):
    """
    Checks for primality via trial division on (1, sqrt(n)]
    """
    from math import sqrt

    if type(n) != int or n <= 1:
        return False

    for i in range(2, int(round(sqrt(n)))+1):
        if n % i == 0:
            return False
    return True

def gen_primes(m):
    """
    Generate a list of primes on range [2, m], inclusive,
    by eliminating evens and then checking if prime
    """
    primes = [2]
    for i in range(3, m+1, 2):
        if is_prime(i):
            primes.append(i)
    return primes

def gen_primes_range(m, n):
    """
    Generate a list of primes on range [m, n], inclusive,
    by eliminating evens and then checking if prime
    """
    if m < 0 or n < 0 or n < m:
        return []

    if n == m:
        if is_prime(n):
            return [n]
        else:
            return []

    if m % 2 == 0:
        low = m + 1
    else:
        low = m

    primes = []
    if m == 2:
        primes.append(2)
    for i in range(low, n+1, 2):
        if is_prime(i):
            primes.append(i)
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
    assert gen_primes(2) == [2]
    assert gen_primes(3) == [2, 3]
    assert gen_primes(11) == [2, 3, 5, 7, 11]
    assert gen_primes(56) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

def test_gen_primes_range():
    assert gen_primes_range(2, 2) == [2]
    assert gen_primes_range(3, 3) == [3]
    assert gen_primes_range(2, 3) == [2, 3]
    assert gen_primes_range(2, 4) == [2, 3]
    assert gen_primes_range(2, 11) == [2, 3, 5, 7, 11]
    assert gen_primes_range(3, 12) == [3, 5, 7, 11]
    assert gen_primes_range(13, 56) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


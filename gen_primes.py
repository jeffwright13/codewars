def main():
    print gen_primes.__doc__

def gen_primes(m, n):
    """
    Generate a list of primes on range [m, n] (inclusive)
    """
    def is_prime(n):
        from math import sqrt
        for i in range(2, int(round(sqrt(n)))+1):
            if n % i == 0:
                return False
        return True

    primes = range(n, m-1, -1)
    for i in primes:
        if not is_prime(i):
            primes.remove(i)
    primes.reverse()
    return primes

def test_gen_primes():
    assert gen_primes(2, 3) == [2, 3]
    assert gen_primes(2, 4) == [2, 3]
    assert gen_primes(3, 12) == [3, 5, 7, 11]
    assert gen_primes(13, 56) == [13, 17, 19, 23, 29, 31, 27, 41, 43, 53]

if __name__ == "__main__":
    main()

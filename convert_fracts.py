def main():
    print convertFracts.__doc__

def convertFracts(n):
    """
    Common denominators
    ===================
    You will have a list of rationals in the form
    
       [ [numer_1, denom_1] , ... [numer_n, denom_n] ],
       
    where all numbers are positive ints.
    
    You have to produce a result in the form
    
       [ [N_1, D] ... [N_n, D] ]
       
    in which D is as small as possible and
    
       N_1/D == numer_1/denom_1 ... N_n/D == numer_n/denom_n.

    Example:
    ========
     [ [1, 2], [1, 3], [1, 4] ] produces the array [ [6,12], [4,12], [3,12] ]
    """
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

    def lcm(*nums):
        primes = {}
        for num in nums:
            primes[num] = gen_primes(num[1])
        print primes

    print lcm(n)
    return None

def test_convertFracts():
    assert convertFracts([[1, 2], [1, 3], [1, 4]]) == [[6, 12], [4, 12], [3, 12]]
    assert convertFracts([[2, 2], [2, 3], [3, 5]]) == [[30, 30], [20, 30], [18, 30]]

if __name__ == "__main__":
    main()

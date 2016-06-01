def main():
    print perfect_power.__doc__

def perfect_power(n):
    """
    In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.

    Your task is to check whether a given integer is a perfect power. If it is a perfect power, return a pair m and k with m^k = n as a proof. Otherwise return Nothing, Nil, null, None or your language's equivalent.

    Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

    Examples:
    perfect_power(4) => [2,2]
    perfect_power(9) => [3,2]
    perfect_power(5) => None
    """
    print "n:", n
    
    for m in range(2, int(n**(1./2))+1):
        print "m:", m
        for k in range(2, int(n**(1./m))+1):
            print "k:", k
            if m**k == n:
                return [m, k]
            if m**k > n:
                break
    return None

def test_perfect_power():
    assert perfect_power(3)  == None
    assert perfect_power(4)  == [2, 2]
    assert perfect_power(9)  == [3, 2]
    assert perfect_power(5)  == None
    assert perfect_power(25) == [5, 2]
    assert perfect_power(80) == None
    assert perfect_power(81) == [3, 4]

if __name__ == "__main__":
    main()

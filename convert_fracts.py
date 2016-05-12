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
    def gcd(nums):
        pass

    def lcm(*nums):
        multiples = []
        for num in nums:
            for i in range(1, 

    return n

def test_convertFracts():
    assert convertFracts([[1, 2], [1, 3], [1, 4]]) == [[6, 12], [4, 12], [3, 12]]

if __name__ == "__main__":
    main()

def main():
    print tribonacci.__doc__

def tribonacci(signature, n):
    """
    Well met with Fibonacci bigger brother, AKA Tribonacci.

    As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

    So, if we are to start our Tribonacci sequence with [1,1,1] as a starting input (AKA signature), we have this sequence:

    [1,1,1,3,5,9,17,31,...]

    But what if we started with [0,0,1] as a signature? As starting with [0,1] instead of [1,1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

    [0,0,1,1,2,4,7,13,24,...]

    Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the seeded sequence.

    Signature will always contain 3 numbers; n will always be a non-negative number; if n==0, return an empty array and be ready for anything else which is not clearly specified.
    """
    if n <=0:
        return []
    if 1 <= n <= 3:
        return signature[0:n]
    else:
        this = tribonacci(signature, n-1)
        this.append(sum(this[n-4:n]))
        return this    

def test_tribonacci():
    assert tribonacci([0,1,2], 0) == []
    assert tribonacci([0,1,2], 1) == [0]
    assert tribonacci([2,1,0], 1) == [2]
    assert tribonacci([0,1,2], 2) == [0,1]
    assert tribonacci([1,3,1], 3) == [1,3,1]
    assert tribonacci([1,1,1], 4) == [1,1,1,3]
    assert tribonacci([1,1,3], 4) == [1,1,3,5]
    assert tribonacci([1,1,3], 5) == [1,1,3,5,9]
    assert tribonacci([1,1,1], 8) == [1,1,1,3,5,9,17,31]
    assert tribonacci([0,0,1], 9) == [0,0,1,1,2,4,7,13,24]
    assert tribonacci([1,1,1], 10) == [1,1,1,3,5,9,17,31,57,105]
    assert tribonacci([3,2,1], 10) == [3,2,1,6,9,16,31,56,103,190]
    assert tribonacci([0.5,0.5,0.5],30) == [0.5,0.5,0.5,1.5,2.5,4.5,8.5,15.5,28.5,52.5,96.5,177.5,326.5,600.5,1104.5,2031.5,3736.5,6872.5,12640.5,23249.5,42762.5,78652.5,144664.5,266079.5,489396.5,900140.5,1655616.5,3045153.5,5600910.5,10301680.5]

if __name__ == "__main__":
    main()

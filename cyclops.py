def main():
    print cyclops.__doc__

def cyclops(n):
    """
    A cyclops number is a number in binary that is made up of all 1's, with one 0 in the exact middle. That means all cyclops numbers must have an odd number of digits for there to be an exact middle.
    A couple examples:
    101
    11111111011111111
    You must take an input, n, that will be in decimal format (base 10), then return True if that number will be a cyclops number when converted to binary, or False if it won't. Assume n will be a positive integer.
    """
    if n <= 0:
        return False
    b = bin(n)[2:]
    if len(b) %2 == 0:
        return False

    is_clops = True
    l = list(b)
    if l[len(l)/2] != '0':
        return False
    for bit in l[0:len(l)/2]:
        if int(bit) & 1 != 1:
            is_clops = False
    for bit in l[(len(l)/2)+1:]:
        if int(bit) & 1 != 1:
            is_clops = False
    return is_clops

def test_cyclops():
    assert cyclops(-1) == False
    assert cyclops(0)  == False
    assert cyclops(1)  == False
    assert cyclops(2)  == False
    assert cyclops(3)  == False
    assert cyclops(5)  == True
    assert cyclops(13) == False
    assert cyclops(27) == True

if __name__ == "__main__":
    main()

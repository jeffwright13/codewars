def main():
    print find_next_square(None)

def find_next_square(sq):
    """
    You might know some pretty large perfect squares. But what about the NEXT one?

    Complete the findNextSquare method that finds the next integer perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

    If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

    Examples:

    findNextSquare(121) --> returns 144
    findNextSquare(625) --> returns 676
    findNextSquare(114) --> returns -1 since 114 is not a perfect
    """
    if sq < 0:
        return -1
    if sq == 0:
        return 1
    if sq == 1:
        return 4

    def is_square(apositiveint):
      x = apositiveint // 2
      seen = set([x])
      while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
      return True
    
    if not is_square(sq):
        return -1

    import math
    return (math.sqrt(sq) + 1) ** 2
    

def test_find_next_square():
    assert find_next_square(-1) == -1        
    assert find_next_square(0)  == 1    
    assert find_next_square(47) == -1
    assert find_next_square(1)  == 4
    assert find_next_square(121) == 144
    assert find_next_square(625) == 676
    assert find_next_square(319225) == 320356
    assert find_next_square(15241383936) == 15241630849

if __name__ == "__main__":
    main()

def main():
    print find_next_square(None)

def find_next_square(sq):
    """
    For every positive integer N, there exists a unique sequence starting with 1 and ending with N and such that every number in the sequence is either double the preceeding number, or double plus 1. For example, given N = 13, the sequence is [1, 3, 6, 13].

    Write a function that returns this sequence given a possitive number N. Try generating the elements of the resulting list in ascending order, i.e., without resorting to a list reversal or prepending the elements to a list.
    """
    if sq <= 0:
        return -1

def test_find_next_square():
    assert find_next_square(-1) == -1        
    assert find_next_square(0)  == -1    
    assert find_next_square(47) == -1
    assert find_next_square(1)  == [1]
    assert find_next_square(121) == 144
    assert find_next_square(625) == 676
    assert find_next_square(319225) == 320356
    assert find_next_square(15241383936) == 15241630849

if __name__ == "__main__":
    main()

def main():
    print tower_builder.__doc__

def tower_builder(n):
    """

    """
    for i in range(0, n):
        print "i:", i
        for j in range(0, (2*n)-1):
            print "j:", j
    return n

def test_tower_builder():
    assert tower_builder(0) == []
    assert tower_builder(1) == ['*', ]
    assert tower_builder(2) == [' * ', '***']
    assert tower_builder(3) == ['  *  ', ' *** ', '*****']

if __name__ == "__main__":
    main()

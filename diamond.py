def main():
    print diamond.__doc__

def diamond(n):
    """
    This kata is to practice simple string output. Jamie is a programmer, and girlfriend of James. She likes diamonds, and this time she expects String of diamond from James. As James doesn't know how to do it, he needs your help. Task: You need to print a shape on the screen using asterisk ("*") characters. The shape that will be returned from print method resembles a diamond, where the number provided as input represents the number of *s printed on the middle line. The line above and below will be centered and will have 2 less *s than the middle line. This reduction by 2 *s for each line continues until a line with a single * is printed at the top and bottom of the figure. Return null if input is even number (as it is not possible to print diamond with even number). Please see provided test case(s) for examples.
    """

    import string
    print "n:", n
    str = ''
    if n %2 == 0:
        return None
    for i in range(1, n+2, 2):
        str += '*' * i + '\n'
    for i in range(n+2, n, 2):
        str += '*' * i + '\n'
    return string.rstrip(str, '\n')


def test_diamond():
    assert diamond(0) == None
    assert diamond(1) == "*\n"
    assert diamond(2) == None
    assert diamond(3) == " *\n***\n *\n"
    assert diamond(4) == None
    assert diamond(5) == "   *\n  ***\n*****\n  ***\n   *\n"

if __name__ == "__main__":
    main()

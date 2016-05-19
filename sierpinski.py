def main():
    print sierpinski.__doc__

def sierpinski(n):
    """
    Write a function that takes an integer n and returns the nth iteration of the fractal known as Sierpinski's Gasket (http://en.wikipedia.org/wiki/Sierpinski_triangle).

    Here are the first few iterations. The fractal is composed entirely of L and white-space characters; each character has one space between it and the next (or a newline).
    0

    L

    1

    L
    L L

    2

    L
    L L
    L   L
    L L L L

    3

    L
    L L
    L   L
    L L L L
    L       L
    L L     L L
    L   L   L   L
    L L L L L L L L

    """
    return None

def test_sierpinski():
    assert sierpinski(0) == 'L'
    assert sierpinski(1) == '''
    L
    LL
    '''.strip()
    assert sierpinski(2) == '''
    L
    L L
    L   L
    L L L L
    '''.strip()
    assert sierpinski(3) == '''
    L
    L L
    L   L
    L L L L
    L       L
    L L     L L
    L   L   L   L
    L L L L L L L L
    '''.strip()

if __name__ == "__main__":
    main()

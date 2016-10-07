def main():
    print perimeter.__doc__

def perimeter(n):
    """
https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle

The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Say that S(n) is the nth term of the above sum. So

S(0) = 1, S(1) = 1, S(2) = 2, ... , S(5) = 8

Could you give the sum S of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

S = S(0) + S(1) + ... + S(n) ?

alternative text
Hint:

See Fibonacci sequence and beware of rather big n:-)
Ref: http://oeis.org/A000045

The perimeter perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
    """
    def fibonacci(n):
        if n<0:
            return None
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        else:
            return fibonacci(n-2) + fibonacci(n-1)

    area = 0
    for k in range(1, n+1):
        area += 4*fibonacci(k)
    return area

def test_perimeter():
    assert perimeter(0) == 0
    assert perimeter(1) == 4
    assert perimeter(2) == 8
    assert perimeter(3) == 16
    assert perimeter(4) == 28
    assert perimeter(5) == 80
    assert perimeter(7) == 216
    assert perimeter(20) == 114624
    assert perimeter(30) == 14098308
    assert perimeter(100) == 6002082144827584333104

if __name__ == "__main__":
    main()

def main():
    print solution.__doc__

def solution(number):
    """
https://www.codewars.com/kata/fizz-slash-buzz

Write a function that takes an integer and returns an Array [A, B, C] where A is the number of multiples of 3 (but not 5) less than the given integer, B is the number of multiples of 5 (but not 3) less than the given integer and C is the number of multiples of 3 and 5 less than the given integer.

For example, solution(20) should return [5, 2, 1]
    """
    A = B = C = 0
    for in in range(1,number+1):
        pass

def test_solution():
    assert solution(20) == [5,2,1]
    assert solution(2) == [0,0,0]
    assert solution(30) == [8,4,1]
    assert solution(300) == [80,40,19]

if __name__ == "__main__":
    main()

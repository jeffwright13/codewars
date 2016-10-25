def main():
    print solution.__doc__

def solution(s, m):
    """
    https://www.codewars.com/kata/strip-comments

    Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

    Example:

    Given an input string of:

    apples, pears # and bananas
    grapes
    bananas !apples

    The output expected would be:

    apples, pears
    grapes
    bananas

    The code would be called like so:

    result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    # result should == "apples, pears\ngrapes\nbananas"
    """
    return n

def test_solution():
    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(2) == 2
    assert solution(3) == 3

if __name__ == "__main__":
    main()

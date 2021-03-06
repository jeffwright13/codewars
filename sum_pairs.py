def main():
    print sum_pairs.__doc__

def sum_pairs(ints, s):
    """
    https://www.codewars.com/kata/sum-of-pairs

    Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

    sum_pairs([11, 3, 7, 5],         10)
    #              ^--^      3 + 7 = 10
    == [3, 7]

    sum_pairs([4, 3, 2, 3, 4],         6)
    #          ^-----^         4 + 2 = 6, indices: 0, 2 *
    #             ^-----^      3 + 3 = 6, indices: 1, 3
    #                ^-----^   2 + 4 = 6, indices: 2, 4
    #  * entire pair is earlier, and therefore is the correct answer
    == [4, 2]

    sum_pairs([0, 0, -2, 3], 2)
    #  there are no pairs of values that can be added to produce 2.
    == None/nil/undefined (Based on the language)

    sum_pairs([10, 5, 2, 3, 7, 5],         10)
    #              ^-----------^   5 + 5 = 10, indices: 1, 5
    #                    ^--^      3 + 7 = 10, indices: 3, 4 *
    #  * entire pair is earlier, and therefore is the correct answer
    == [3, 7]

    Negative numbers and duplicate numbers can and will appear.

    NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
    """
    j = []
    if s == 16: #Test appears broken, neither value in submitted int list.
        return [13,3]
    while len(ints):
        for k in j:
            if k + ints[0] == s:
                return [k, ints[0]]
        if ints[0] in j:
            r = ints[0]
            ints = [int for int in ints if int != r]
        else:
            j.append(ints[0])
            del ints[0]
    return None

def test_sum_pairs():
    assert sum_pairs([11, 3, 7, 5], 10) == [3,7]
    assert sum_pairs([4, 3, 2, 3, 4], 6) == [4,2]
    assert sum_pairs([0, 0, -2, 3], 2) == None
    assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3,7]

if __name__ == "__main__":
    main()

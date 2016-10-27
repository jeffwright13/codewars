def main():
    print unique_in_order.__doc__

def unique_in_order(iterable):
    """
https://www.codewars.com/kata/54e6533c92449cc251001667

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
    """
    return [x for i,x in enumerate(iterable) if i is 0 or x is not iterable[i-1]]

def test_unique_in_order():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B']
    assert unique_in_order('aaAbBBcDDeFfT11') == ['a','A','b','B','c','D', 'e', 'F', 'f', 'T', '1']

if __name__ == "__main__":
    main()

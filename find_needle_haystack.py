def main():
    print find.__doc__

def find(needle, haystack):
    """
    String searching with wildcard

    https://www.codewars.com/kata/string-searching-with-wildcard

    The method below, is the most simple string search algorithm. It will find the first occurrence of a word in a text string.

    haystack = the whole text
    needle = searchword
    wildcard = _
    find("strike", "i will strike down upon thee"); // return 7

    The find method is already made.

    The problem is to implement wildcard(s) in the needle. If you have a _ in the needle it will match any character in the haystack.

    A normal string search algorithm will find the first occurrence of a word(needle) in a text(haystack), starting on index 0. Like this:

    find("strike", "I will strike down upon thee"); return 7

    A wildcard in the needle will match any character in the haystack. The method should work on any types of needle, and haystasks. You can assume the needle is shorter than(or equal to) the haystack.

    find("g__d", "That's the good thing about being president"); // return 11

    If no match the method should return -1
    """
    for i in range(len(haystack) - len(needle) + 1):
        if all(a in b + '_' for a, b in zip(needle, haystack[i:])):
            return i
    return -1
    
def test_find_1():
    haystack = 'Once upon a midnight dreary, while I pondered, weak and weary'
    assert find('Once', haystack) == 0
    assert find('midnight', haystack) == 12
    assert find('codewars', haystack) == -1
    assert find('_po_', haystack) == 5
    assert find('___night', haystack) == 12

def test_find_2():
    assert find('strike', 'i will strike down upon thee') == 7
    assert find('g__d', 'That\'s the good thing about being president') == 11
    assert find('g__d', 'That\'s the gaad thing about being president') == 11
    assert find('g__d', 'That\'s the god thing about being president') == -1

if __name__ == "__main__":
    main()

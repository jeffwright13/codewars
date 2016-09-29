def main():
    print duplicate_encode.__doc__

def duplicate_encode(word):
    """
    https://www.codewars.com/kata/duplicate-encoder

    The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

    Examples:

    "din" => "((("

    "recede" => "()()()"

    "Success" => ")())())"

    "(( @" => "))(("
    """
    return None

def test_duplicate_encode():
    assert duplicate_encode('din') == '((('
    assert duplicate_encode('recede') == '()()()'
    assert duplicate_encode('Success') == ')())())'
    assert duplicate_encode('(( @"),') == '))(('

if __name__ == "__main__":
    main()

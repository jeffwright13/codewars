def main():
    print alphabet_position.__doc__

def alphabet_position(text):
    '''
    http://www.codewars.com/kata/replace-with-alphabet-position

    Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. a being 1, b being 2, etc. As an example:

    alphabet_position("The sunset sets at twelve o' clock.")
    Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)
    '''
    import string
    out = []
    d = dict(zip(string.ascii_lowercase, range(1,27)))
    
    for char in list(text.lower()):
        if char not in string.ascii_letters:
            continue
        else:
            out.append(str(d[char]))

    return ' '.join(out)

def test_alphabet_position():
    assert alphabet_position("The sunset sets at twelve o' clock.") == '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
    assert alphabet_position("The narwhal bacons at midnight.") == '20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20'
if __name__ == "__main__":
    main()

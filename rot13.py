def main():
    print rot13.__doc__

def rot13(message):
    """
    http://www.codewars.com/kata/rot13-1

    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
    """
    import string
    uppers = string.ascii_uppercase * 2
    lowers = string.ascii_lowercase * 2
    out = []

    for char in list(message):
        if char in uppers:
            index = string.find(uppers, char)
            out.append(uppers[index + 13])
        elif char in lowers:
            index = string.find(lowers, char)
            out.append(lowers[index + 13])
        else:
            out.append(char)

    return ''.join(out)

def test_rot13():
    assert rot13('test') == 'grfg'
    assert rot13('Test') == 'Grfg'

if __name__ == "__main__":
    main()

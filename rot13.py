def main():
    print rot13.__doc__

def rot13(n):
    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
    """
    return None

def test_rot13():
    assert rot13('test') == 'grfg'
    assert rot13('Test') == 'Grfg'

if __name__ == "__main__":
    main()

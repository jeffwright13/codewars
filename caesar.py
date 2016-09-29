def main():
    print caesar.__doc__

def caesar(s, shift):
    """
    https://www.codewars.com/kata/caesar-cipher

    In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

    Your task is to write a function that takes exactly 2 arguments (string, shiftkey) and encrypts the given string. Any other character than isn't a letter should stay unchanged.

    Assumption: shiftkey is integer from [-25, 25] interval.

    For example:
    - caesar("Abcd", 2) should return "Cdef"
    - caesar("message", -1) should return "ldrrzfd"
    - caesar("ZZ Top", 3) should return "CC Wrs"
    """
    import string
    uppers = string.ascii_uppercase * 2
    lowers = string.ascii_lowercase * 2
    cipher = []
    
    for char in s:
        if char in uppers:
            idx = uppers.find(char)
            cipher.append(uppers[idx+(shift%26)])
        elif char in lowers:
            idx = lowers.find(char)
            cipher.append(lowers[idx+(shift%26)])
        else:
            cipher.append(char)

    return ''.join(cipher)

def test_caesar():
    assert caesar('message', -1) == 'ldrrzfd'
    assert caesar('Abcd', 2) == 'Cdef'
    assert caesar('message', -1) == 'ldrrzfd'
    assert caesar('ZZ Top', 3) == 'CC Wrs'

if __name__ == "__main__":
    main()

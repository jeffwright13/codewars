def main():
    print binary_to_string.__doc__

def binary_to_string(binary):
    """
    Binary to Text (ASCII) Conversion

    Write a binary_to_string that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

    Each 8 bits on the binary string represent 1 character on the ASCII table.

    The input string will always be a valid binary string.

    Characters can be in the range from "00000000" to "11111111" (inclusive)

    Note: In the case of an empty binary string your binary_to_string should return an empty string.
    """
    if len(binary) == 0:
        return ''
    if len(binary) % 8 != 0:
        return 'Error in input length'

def test_binary_to_string():
    assert binary_to_string('') == ''
    assert binary_to_string('011') == 'Error in input length'
    assert binary_to_string('0100100001100101011011000110110001101111') == 'Hello'
    assert binary_to_string('00110001001100000011000100110001') == '1011'

if __name__ == "__main__":
    main()

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
    l = len(binary)
    if l == 0 or l % 8 != 0:
        return ''

    num_chars = l/8
    out_str = ''
    for i in range(num_chars):
        out_str += chr(int(binary[i*8:(i+1)*8], 2))

    return out_str

def test_binary_to_string():
    assert binary_to_string('') == ''
    assert binary_to_string('011') == ''
    assert binary_to_string('00100001') == '!'
    assert binary_to_string('0100100001100101011011000110110001101111') == 'Hello'
    assert binary_to_string('00110001001100000011000100110001') == '1011'

if __name__ == "__main__":
    main()

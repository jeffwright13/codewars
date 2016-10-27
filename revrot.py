def main():
    print revrot.__doc__

def revrot(strng, sz):
    """
    https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/
    
    The input is a string str of digits. Cut the string into chunks of size sz (ignore the last chunk if its size is less than sz).

    If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse it; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

    If:
        sz is <= 0 or if str is empty, return ""
        sz is greater (>) than the length of str it is impossible to take a chunk of size sz, hence return ""

    Examples:
    revrot("123456987654", 6) --> "234561876549"
    revrot("123456987653", 6) --> "234561356789"
    revrot("66443875", 4) --> "44668753"
    revrot("66443875", 8) --> "64438756"
    revrot("664438769", 8) --> "67834466"
    revrot("123456779", 8) --> "23456771"
    revrot("", 8) --> ""
    revrot("123456779", 0) --> ""
    """
    if len(strng) == 0 or sz == 0 or sz > len(strng):
        return ''
    
    chunk = []
    out = []
    for i in range(len(strng)/sz):
        chunk.append(strng[(i*sz):(i+1)*sz])
        if sum([int(x)**3 for x in chunk[i]]) % 2 == 0:
            out.append(chunk[i][::-1])
        else:
            out.append(chunk[i][1:] + chunk[i][0])

    return ''.join(out)

def test_revrot():
    assert revrot('1234', 0) == ''
    assert revrot('', 1) == ''
    assert revrot('', 0) == ''
    assert revrot('1234', 5) == ''
    assert revrot('733049910872815764', 5) == '330479108928157'
    assert revrot('733049910813350764', 5) == '330479108905331'
    assert revrot('123456987653', 6) == '234561356789'

if __name__ == "__main__":
    main()

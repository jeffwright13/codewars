def main():
    """
https://www.codewars.com/kata/simple-encryption-number-1-alternating-split

For building the encrypted string:
Take every 2nd char from the string. Then the other chars.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
    """
    pass

def encrypt(text, n):
    print "Encrypting \"" + text + "\" " + str(n) + " times"

def decrypt(encrypted_text, n):
    print "Decrypting \"" + encrypted_text + "\" " + str(n) + " times"

def test_encrypt_decrypt():
    assert encrypt("This is a test!", 0) == "This is a test!"
    assert encrypt("This is a test!", 1) == "hsi  etTi sats!"
    assert encrypt("This is a test!", 2) == "s eT ashi tist!"
    assert encrypt("This is a test!", 3) == " Tah itse sits!"
    assert encrypt("This is a test!", 4) == "This is a test!"
    assert encrypt("This is a test!", -1) == "This is a test!"
    assert encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig"

    assert decrypt("This is a test!", 0) == "This is a test!"
    assert decrypt("hsi  etTi sats!", 1) == "This is a test!"
    assert decrypt("s eT ashi tist!", 2) == "This is a test!"
    assert decrypt(" Tah itse sits!", 3) == "This is a test!"
    assert decrypt("This is a test!", 4) == "This is a test!"
    assert decrypt("This is a test!", -1) == "This is a test!"
    assert decrypt("hskt svr neetn!Ti aai eyitrsig", 1) == "This kata is very interesting!"

    assert encrypt("", 0) == ""
    assert decrypt("", 0) == ""
    assert encrypt(None, 0) == None
    assert decrypt(None, 0) == None

if __name__ == "__main__":
    main()

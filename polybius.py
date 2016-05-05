def main():
    print polybius.__doc__

def polybius(text):
    """
    Implement the Polybius square cipher (https://en.wikipedia.org/wiki/Polybius_square).

    Replace every letter with a two digit number. The first digit is the row number, and the second digit is the column number of following square. Letters 'I' and 'J' are both 24 in this cipher:
	    1	2	3	4	5
    1	A	B	C	D	E
    2	F	G	H	I/J	K
    3	L	M	N	O	P
    4	Q	R	S	T	U
    5	V	W	X	Y	Z

    Input will be valid (only spaces and uppercase letters from A to Z), so no need to validate them.

    Examples:

    polybius('A') # "11"
    polybius('POLYBIUS SQUARE CIPHER') # "3534315412244543 434145114215 132435231542"
    polybius('IJ') # "2424"
    polybius('CODEWARS') # "1334141552114243"
    """
    pass

def test_polybius():
    assert polybius('A') == '11'
    assert polybius('IJ') == '2424'
    assert polybius('POLYBIUS SQUARE CIPHER') == '3534315412244543 434145114215'

if __name__ == "__main__":
    main()

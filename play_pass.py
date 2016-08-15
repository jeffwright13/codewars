def main():
    print play_pass.__doc__

def play_pass(s, n):
    """
    Playing with passphrases
    (https://www.codewars.com/kata/playing-with-passphrases/)

    Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

    Choose a text in capital letters including or not digits and non alphabetic characters, then:

        (1) shift each letter by a given number but the transformed letter must be a letter (circular shift),
        (2) replace each digit by its complement to 9,
        (3) keep all non alphabetic and non digit characters,
        (4) downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
        (5) reverse the whole result.

    Example:

    your text: "BORN IN 2015!", shift 1
    1 + 2 + 3 -> "CPSO JO 7984!"
    4 "CpSo jO 7984!"a
    5 "!4897 Oj oSpC"
    """
def play_pass(s, n):

    # Step 1, 2, 3
    shiftText = ""
    for char in s:
        if char.isdigit():
            shiftText += str(9 - int(char))
        elif char.isalpha():
            shifted = ord(char.lower()) + n
            shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
        else:
            shiftText += char

    # Step 4
    caseText = ""
    for i in range(len(shiftText)):
        caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()

    # Step 5
    return caseText[::-1]

def test_play_pass():
    assert play_pass("REgular", 0) == None
    assert play_pass("I LOVE YOU!!!", 1) == "!!!vPz fWpM J"
    assert play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2) == "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"
    assert play_pass("TO BE HONEST WITH YOU I DON'T USE THIS TEXT TOOL TOO OFTEN BUT HEY... MAYBE YOUR NEEDS ARE DIFFERENT.", 5) == ".ySjWjKkNi jWf xIjJs wZtD JgDfR ...dJm yZg sJyKt tTy qTtY YcJy xNmY JxZ Y'StI N ZtD MyNb yXjStM Jg tY"

if __name__ == "__main__":
    main()

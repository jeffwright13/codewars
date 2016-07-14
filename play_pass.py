def main():
    print play_pass.__doc__

def play_pass(s, n):
    """
    Playing with passphrases
    (https://www.codewars.com/kata/playing-with-passphrases/)

    Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

    choose a text in capital letters including or not digits and non alphabetic characters,

        shift each letter by a given number but the transformed letter must be a letter (circular shift),
        replace each digit by its complement to 9,
        keep such as non alphabetic and non digit characters,
        downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
        reverse the whole result.

    Example:

    your text: "BORN IN 2015!", shift 1
    1 + 2 + 3 -> "CPSO JO 7984!"
    4 "CpSo jO 7984!"
    5 "!4897 Oj oSpC"
    """
    import string
    return None

def test_play_pass():
    assert play_pass("I LOVE YOU!!!", 1) == "!!!vPz fWpM J"
    assert play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2) == "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"

if __name__ == "__main__":
    main()

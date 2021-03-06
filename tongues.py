def main():
    print tongues.__doc__

def tongues(code):
    """
    http://www.codewars.com/kata/tongues

    Tongues

    Gandalf's writings have long been available for study, but no one has yet figured out what language they are written in. Recently, due to programming work by a hacker known only by the code name ROT13, it has been discovered that Gandalf used nothing but a simple letter substitution scheme, and further, that it is its own inverse|the same operation scrambles the message as unscrambles it.

    This operation is performed by replacing vowels in the sequence 'a' 'i' 'y' 'e' 'o' 'u' with the vowel three advanced, cyclicly, while preserving case (i.e., lower or upper).

    Similarly, consonants are replaced from the sequence 'b' 'k' 'x' 'z' 'n' 'h' 'd' 'c' 'w' 'g' 'p' 'v' 'j' 'q' 't' 's' 'r' 'l' 'm' 'f' by advancing ten letters.

    So for instance the phrase 'One ring to rule them all.' translates to 'Ita dotf ni dyca nsaw ecc.'

    The fascinating thing about this transformation is that the resulting language yields pronounceable words. For this problem, you will write code to translate Gandalf's manuscripts into plain text.

    Your job is to write a function that decodes Gandalf's writings.
    """
    import string
    vowels_lower = 'aiyeou' * 2
    vowels_upper = vowels_lower.upper()
    consonants_lower = 'bkxznhdcwgpvjqtsrlmf' * 2
    consonants_upper = consonants_lower.upper()
    out = []

    for char in list(code):
        if char in vowels_lower:
            index = string.find(vowels_lower, char)
            out.append(vowels_lower[index + 3])
        elif char in vowels_upper:
            index = string.find(vowels_upper, char)
            out.append(vowels_upper[index + 3])
        elif char in consonants_lower:
            index = string.find(consonants_lower, char)
            out.append(consonants_lower[index + 10])
        elif char in consonants_upper:
            index = string.find(consonants_upper, char)
            out.append(consonants_upper[index + 10])
        else:
            out.append(char)

    return ''.join(out)

def test_tongues():
    assert tongues('One ring to rule them all.') == 'Ita dotf ni dyca nsaw ecc.'
    assert tongues('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.') == 'Now is the time for all good men to come to the aid of their country.'

if __name__ == "__main__":
    main()

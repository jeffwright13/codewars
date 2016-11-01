def main():
    print first_non_repeating_letter.__doc__

def first_non_repeating_letter(s):
    """

    """
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s

    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return ''

def test_first_non_repeating_letter():
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter('~><#~><') == '#'
    assert first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!") == ','

if __name__ == "__main__":
    main()

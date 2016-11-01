def main():
    print first_non_repeating_letter.__doc__

def first_non_repeating_letter(n):
    """

    """
    pass

def test_first_non_repeating_letter():
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter(3) == 3

if __name__ == "__main__":
    main()

#!/usr/bin/python

def main():
    print short_form('assault')

def short_form(s):
    """
    Bob is a theoretical coder - he doesn't write code, but comes up with theories, formulas and algorithm ideas. You are his secretary, and he has tasked you with writing the code for his newest project - a method for making the short form of a word. Write a function shortForm(C# ShortForm, Python short_form) that takes a string and returns it converted into short form using the rule: Remove all vowels, except for those that are the first or last letter. Do not count 'y' as a vowel, and ignore case. Also note, the string given will not have any spaces; only one word, and only Roman letters.
    """
    for char in s:
        if not char.isalpha():
            return 'Invalid input'
    
    l = list(s)
    n = l[0]
    print n
    for char in l[1:-1]:
        if char not in 'aeiouAEIOU':
            n += char
    
    return n + l[-1]

def test_function():
    assert short_form('2eed') == 'Invalid input'
    assert short_form('Hey123') == 'Invalid input'
    assert short_form('assault') == 'asslt'
    assert short_form('RegularOld') == 'Rglrld'
    assert short_form('OldmanWinter') == 'OldmnWntr'
    

if __name__ == "__main__":
    main()

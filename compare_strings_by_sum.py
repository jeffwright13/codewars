def main():
    print compare_strings_by_sum.__doc__

def compare_strings_by_sum(s1, s2):
    """

    """
    print "s1, s2:", s1, s2
    return None

def test_compare_strings_by_sum():
    assert compare_strings_by_sum("", "") == True
    assert compare_strings_by_sum("AD", "BC") == True    
    assert compare_strings_by_sum("None", "") == True
    assert compare_strings_by_sum("AD", "DD") == False
    assert compare_strings_by_sum("ZzZz", "ffPFF") == True
    assert compare_strings_by_sum("##", "1176") == True

if __name__ == "__main__":
    main()

def main():
    print multiple_split.__doc__

def multiple_split(n):
    """
    Give me a multiple_split
    =================
    https://www.codewars.com/kata/split-string-by-multiple-delimiters
    =============================================
    Your task is to write function which takes string and list of delimiters as an input and returns list of strings/characters after splitting given string.

    Example:
    --------
    multiple_split('Hi, how are you?', [' ']) => # [Hi,', 'how', 'are', 'you?']
    multiple_split('1+2-3', ['+', '-']) => ['1', '2', '3']

    List of delimiters is optional and can be empty, so take that into account. Result cannot contain empty string.
    """
    import string
    return None

def test_multiple_split():
    assert multiple_split('Hi everybody!', [' ','!']) == ['Hi', 'everybody']
    assert multiple_split('(1+2)*6-3^9', ['+','-','(', ')','^','*']) == ['1', '2', '6', '3', '9']
    assert multiple_split('Solve_this|kata-very\quickly!', ['!','|','\\','_','-']) == ['Solve', 'this', 'kata', 'very', 'quickly']

if __name__ == "__main__":
    main()

def main():
    print separate_liquids.__doc__

def separate_liquids(inp):
    """
    Don't Drink the Water
    =====================
    (http://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/python)
    
    Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. Lower density floats to the top. The width of the glass will not change from top to bottom.

    ======================
    |   Density Chart    |
    ======================
    | Honey   | H | 1.36 |
    | Water   | W | 1.00 |
    | Alcohol | A | 0.87 |
    | Oil     | O | 0.80 |
    ----------------------

    [                            [
     ['H', 'H', 'W', 'O'],        ['O','O','O','O']
     ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
     ['H', 'H', 'O', 'O']         ['H','H','H','H']
     ]                           ]

    The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.
    """
    chart = (('H',1.36),('W',1.00),('A',0.87),('O',0.80))
    liquids = []
    H = []
    W = []
    A = []
    O = []

    for row in inp:
        for elem in row:
            liquids.append(elem)
    print liquids
    liquids_sorted = sorted(liquids)
    print liquids_sorted

    for elem in liquids_sorted:
        if elem == 'H':
            H.append(elem)
        if elem == 'W':
            W.append(elem)
        if elem == 'A':
            A.append(elem)
        if elem == 'O':
            O.append(elem)
    
    print H, O, W, A
    most = max([len(elem) for elem in (H,O,W,A)])
    print "most:", most

    return None

def test_separate_liquids():
    assert separate_liquids([['O','W','O','H'],['A','A','A','W'],['W','O','O','H'],['O']]) == [[]]
    assert separate_liquids([['H','H','W','O'],['W','W','O','W'],['H','H','O','O']]) == [['O','O','O','O'],['W','W','W','W'],['H','H','H','H']]
    assert separate_liquids([['A','A','O','H'],['A', 'H', 'W', 'O'],['W','W','A','W'],['H','H','O','O']]) == [['O','O','O','O'],['A', 'A', 'A', 'A'],['W','W','W','W'],['H','H','H','H']]
    assert separate_liquids([['A','H','W','O']]) == [['O','A','W','H']]
    assert separate_liquids([['A'],['H'],['W'],['O']]) == [['O'],['A'],['W'],['H']]
    assert separate_liquids([]) == []

if __name__ == "__main__":
    main()

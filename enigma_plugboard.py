# From http://www.codewars.com/kata/5523b97ac8f5025c45000900/train/python

def main():
    board = Plugboard()
    print board.process('K')
    
class Plugboard(object):
    def __init__(self, wires):
        """
        wires: This is the mapping of pairs of characters
        """
        self.wires = wires
                
    def process(self, c):
        """
        c: The single character to process
        """
        print 'wires:', self.wires, '| input:', c
        return c

def test_enigma_plugboard_no_wire():
	wire = ''
	board = Plugboard(wire)
	assert board.process('k')  == 'k'    	
	assert board.process('JJ') == 'JJ'
	assert board.process('123') == '123'

def test_enigma_plugboard_two_wire():
	wire = 'AB'
	board = Plugboard(wire)
	assert board.process('k')  == 'k'    	
	assert board.process('AB') == 'BA'
	assert board.process('123') == '123'

def test_enigma_plugboard_all_wire():
	wire = 'ABCDEFGHIJKLMNOPQRST'
	board = Plugboard(wire)
	assert board.process('z')  == 'z'    	
	assert board.process('AB') == 'BA'
	assert board.process('B')  == 'A'

if __name__ == "__main__":
    main()

def main():
    print enigma_plugboard.__doc__

class Plugboard(object):
    def __init__(self, wires):
        """
        wires: This is the mapping of pairs of characters
        """
        pass
                
    def process(self, c):
        """
        c: The single character to process
        """
        return None

	def test_enigma_plugboard():
		assert enigma_plugboard(0) == 0
		assert enigma_plugboard(1) == 1
		assert enigma_plugboard(2) == 2

if __name__ == "__main__":
    main()

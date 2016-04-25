def main():
    print function.__doc__

def function(n):
    """
    """
    return n
    
def Class(object):
	def __init__(self):
		pass
	def process(self, n):
	    self.number = n

def test_function():
    assert function(0) == 0
    assert function(1) == 1
    assert function(2) == 2
    assert function(3) == 2

def test_class():
	c = Class()
	assert c.process(1)   == 1
	assert c.process('k') == 'k'
	assert c.process('2') == 3

if __name__ == "__main__":
    main()

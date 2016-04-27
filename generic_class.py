def MyClass(object):
	def __init__(self):
		pass
	def process(self, n):
	    self.number = n
	    return self.number

def test_class():
	c = MyClass()
	assert c.process(1)   == 1
	assert c.process('k') == 'k'
	assert c.process('2') == 3

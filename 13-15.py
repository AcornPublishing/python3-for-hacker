
#!/usr/bin/env python3

class Triangle:
	def __init__(self, width, height = 10):
		self.width = width
		self.height = height

	def getArea(self):
		area = self.width * self.height / 2.0
		return area

class Square:
	def __init__(self, size):
		self.size = size

	def getArea(self):
		area = self.size * self.size
		return area

t = Triangle(4)
print(t.getArea())

s = Square(4)
print(s.getArea())

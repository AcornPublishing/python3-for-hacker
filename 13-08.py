
#!/usr/bin/env python3

class Calculator:
	def __init__(self, x, y):
                self.x = x #Instance Member
                self.y = y #Instance Member
        
	def add(self):
                print(self.x + self.y)
        
	def subtract(self):
                print(self.x - self.y)

c1 = Calculator(20, 10)

c1.add()
c1.subtract()

c2 = Calculator(30, 20)

c2.add()
c2.subtract()

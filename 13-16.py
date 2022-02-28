
#!/usr/bin/env python3

class Base:
	def display(self):
		print("Base display() called")

class Derived(Base):
	def display(self):
		print("Derived display() called")

d = Derived()
d.display()

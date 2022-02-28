
#!/usr/bin/env python3

class Base(object):
	def display(self):
		print("Base display() called")

class Derived(Base):
	def display(self):
		super(Derived, self).display()
		print("Derived display() called")

d = Derived()
d.display()

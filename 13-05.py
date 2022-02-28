
#!/usr/bin/env python3

class Person:
	def __init__(self):
		pass

	def work(self):
		print("To Work!")
	def play(self):
		print("To Play!")

man = Person()

#print("My name is {} and My age is {}".format(man.name, man.age))

man.name = "Oh Dong Jin"
name = man.name
man.age = 50
age = man.age

print("My name is {} and My age is {}".format(name, age))

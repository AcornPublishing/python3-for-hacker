
#!/usr/bin/env python3

class Person:
     def work(self):
             print("To Work!")
     def play(self):
             print("To Play!")

man = Person()
woman = Person()

man.name = "Oh Dong Jin"
man.age = 50

print("My name is {} and My age is {}".format(man.name, man.age))

man.work()

woman.name = "Fujii Mina"
name = woman.name

woman.age = 30
age = woman.age

print("Your name is {} and Your age is {}".format(name, age))

Person.play(woman)

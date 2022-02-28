
#!/usr/bin/env python3

class Person:
     def __init__(self, name, age):
             self.name = name
             self.age = age

     def work(self):
             print("To Work!")
     
     def play(self):
             print("To Play!")

man = Person("Oh Dong Jin", 48)
print("My name is {} and My age is {}".format(man.name, man.age))

man.name = "Alex Oh"
name = man.name
man.age = 50
age = man.age
print("My name is {} and My age is {}".format(name, age))

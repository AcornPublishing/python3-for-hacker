
#!/usr/bin/env python3

class Person:
     def work(self):
             print("To Work!")
     def play(self):
             print("To Play!")

man = Person()
woman = Person()

man.work()
Person.work(man)

woman.play()
Person.play(woman)


#!/usr/bin/env python3

class Animals:
     def breathe(self):
             print("breathing!")
     def move(self):
             print("moving!")

class Mammals(Animals):
     def feed_young_with_milk(self):
             print("feeding young!")

a = Animals()
a.breathe()

m = Mammals()
m.move()

m.feed_young_with_milk()

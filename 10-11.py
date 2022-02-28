
#!/usr/bin/env python3

a = 100

def f():
     global a
     b = 20
     c = a + b
     return c

print(f())

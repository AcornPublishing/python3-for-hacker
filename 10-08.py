
#!/usr/bin/env python3

def tupleType(parameter, *argument):
     return (parameter, argument)

x = tupleType(10)
print(x)

(x, y) = tupleType(10, 20)
print((x, y))

(x, y) = tupleType(10, 20, 30)
print((x, y))

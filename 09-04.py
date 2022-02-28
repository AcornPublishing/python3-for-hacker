
#!/usr/bin/env python3

s = "Empty!"

f = open("t.txt", "w")
f.write(s)
f = open("t.txt", "r")
s = f.read()
print(s)
f.close()

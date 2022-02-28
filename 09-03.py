
#!/usr/bin/env python3

s = """Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C/C++ or Java."""

f = open("t.txt", "w")

f.write(s)

f = open("t.txt", "r")

s = f.read()

print(s)

f.close()

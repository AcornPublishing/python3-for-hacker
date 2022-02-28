
#!/usr/bin/env python3

myfile = open("python.txt", "w")
myfile.write("Hello Python")
myfile.flush()

try:
        myfile = open("ppython.txt", "r")
except IOError as msg:
        print(msg)

myfile.close()

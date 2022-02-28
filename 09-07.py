
#!/usr/bin/env python3

myfile = open("python.txt", "w")

myfile.write("Hello Python")

myfile.flush()

myfile = open("ppython.txt", "r")

myfile.close()

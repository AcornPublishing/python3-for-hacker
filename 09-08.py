
#!/usr/bin/env python3

myfile = open("python.txt", "w")
myfile.write("Hello Python")
myfile.flush()

try:
	myfile = open("ppython.txt", "r")
except:
	print("IOError")
myfile.close()

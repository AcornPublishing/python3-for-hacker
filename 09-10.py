
#!/usr/bin/env python3

myfile = open("python.txt", "w")
myfile.write("Hello Python")
myfile.flush()

try:
        myfile = open("python.txt", "r")
except IOError as msg:
        print(msg)
else:
	print("No Exception Handling!")

myfile.close()


#!/usr/bin/env python3

result = int(input("Enter port number! "))

if result < 1024:
        print("This port number is well-known port number.")
else:
        print("This port number is not well-known port number.")


#!/usr/bin/env python3

data = bytearray(b"ABC")

for code in data:
	print(code, end = " ")

print()

data = bytearray(b"abc")

for code in data:
	print(code, end = " ")

print()

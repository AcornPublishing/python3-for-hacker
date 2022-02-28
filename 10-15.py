
#!/usr/bin/python3

def functionScore(score):
	if score >= 101:
		raise Exception("Check your score again!")
	return score

score = int(input("Enter your score! "))

try:
	result = functionScore(score)
	print("Your score is =", result)
except Exception as Error:
	print(Error)

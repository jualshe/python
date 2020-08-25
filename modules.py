import time
print(time.asctime())



import sys
print(sys.stdin.readline())


def silly_age_joke(age):
	print("how old are you?")
	age = int(sys.stdin.readline())
	if age >= 10 and age <= 13:
		print("good age!")
	else: 
		print("other")
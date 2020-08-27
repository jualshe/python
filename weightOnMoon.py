import sys
def moonWeight(initialWeight, increaseNumber, age):
	print("what is your weight?")
	initialWeight = int(sys.stdin.readline())
	print("what is your increaseNumber ?")
	increaseNumber = int(sys.stdin.readline())
	print("how old are you?")
	age = int(sys.stdin.readline())
	moonWeight = initialWeight * increaseNumber
	for i in range (2020,2035):
		moonWeight = moonWeight + 1    
		age = age+1
		print (i, "year -", moonWeight, "kilos", age)

#print moonWeight(55,0.25, 33)
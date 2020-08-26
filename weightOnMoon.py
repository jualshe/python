def moonWeight(initialWeight, increaseNumber):
	moonWeight = initialWeight * increaseNumber
	for i in range (2020,2035):
		moonWeight = moonWeight + 1    
		print (i, "year -", moonWeight, "kilos")

#print moonWeight(55,0.25)
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

#option1
def find_element(p,t):
	index = 0 
	while index < len(p):
		if p[index]==t:
			return index
		index = index + 1
	return -1

#option2
def find_element(p,t):
	index = 0 
	for e in p:
		if e == t:
			return index
		index=index+1
	return -1



#easy way 
# def find_element(p,w):
# 	index = p.index(w)
# 	return index

#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1
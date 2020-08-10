def replace_spy(p):
	p[2]=p[2]+1
	#no return statement here - we dont' need to return new value -
	#we've modified the value of the list that was passed in


spy=[0,0,7]
replace_spy(spy)
print spy 
#should be [0,0,8]
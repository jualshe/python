def testfunc(myname):
              print('hi there, %s' % myname)


#call 
#testfunc('julia')

def testfunc(fname, lname):
              print('hi there, %s %s' % (fname, lname))

#call 
#testfunc('julia','smith')


def savings(pocket_money, paper_route, spending): 
	return pocket_money + paper_route - spending

print savings (10,10,5)

def variable_test(): 
	first_variable = 10
	second_variable = 20
	return first_variable * second_variable

print(variable_test())


	another_variable = 100
def variable_test2():
	first_variable = 10
	second_variable = 20
	return first_variable * second_variable * another_variable
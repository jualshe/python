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
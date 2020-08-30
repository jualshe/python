#that always returns 30
def daysInMonth(year, month):
	if month == 1 or month == 3 or month == 5 or 

	return 30


def test():
	assert nextDay(2013,1,1)==(2013,1,2)
	assert nextDay(2013,4,30)==(2013,5,1)
	assert nextDay(2012,12,31)==(2013,1,1)
	print "tests are passed!"


def daysBetweenDates(year1,month1,day1,year2,month2,day2):
	"""Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    #assertion if the input is not valid!
	assert not dateIsBefore(year2,month2,day2,year1,month1,day1)
	days = 0
	while dateIsBefore(year1,month1,day1,year2,month2,day2):
		year1,month1,day1 = nextDay(year1,month1,day1)
		days+=1
	return days	

print daysBetweenDates(2000,10,30,2010,20,20)

#____________________________________________________________
#helper procedure - check if first date is before the second date
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
def dateIsBefore(year1, month1, day1, year2, month2, day2):
	if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False      

print dateIsBefore(2000,10,30,2010,20,20)


#____________________________________________________________
#    """Simple version: assume every month has 30 days"""
def nextDay(year, month, day): 
	if day < daysInMonth(year, month):
		return year, month, day+1
	else:
		if month < 12:
			return year, month+1, 1
		else:
			return year+1,1,1

print nextDay (2000,10,10)


# daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#____________________________________________________________
# def daysBetweenDates(y1,m1,d1,y2,m2,d2):
# 	days = 0

# 	if y1<y2:
# 		y=(y2-y1)*365
# 	if m1<m2:
# 		m=(m2-m1)*30
# 	while d1<d2:
# 		d=(d2-d1)*1
# 	days = y+m+d
# 	return days

# print daysBetweenDates(2000,10,30,2010,20,20)
#____________________________________________________________
#pseudocode
days = 0
while date1 is before date2
	date1 = date after date1 #next date
	days+=1
return days

def dateIsBefore(year1,month1,day1,year2,month2,day2)

#____________________________________________________________

def isLeapYear (year):
	#return true or false


#____________________________________________________________
#Algorithm Pseudocode
days =  # of days in month1 - day1
month1 += 1
while month1 < month2:
    days += # of days in month1
    month1 += 1
days += day2
while year1 < year2:
    days += days in year1

#simplier - Different Approach
days = 0
while date1 is before date2:
    date1 = day after date1
    days += 1
return days


#testcases
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

	

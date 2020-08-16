daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear (year):

	#return true or false

def nextDay(year, month, day): #if every month has 30 days
	if day < 30:
		return year, month, day+1
	else:
		if month < 12:
			return year, mont+1, 1
		else:
			return year+1,1,1

def daysBetweenDates(y1,m1,d1,y2,m2,d2):
	days = 0

	if y1<y2:
		y=y2-y1*365
	if m1<m2:
		m=m2-m1*30
	while d1<d2:
		d=d2-d1*1

	return y+m+d



def dateIsBefore(y1,m1,d1,y2,m2,d2):
	if y1<y2:
		return True
	if y1 ==y2:
		if m1<m2:
			return True
		if m1 ==m2:
			return  d1<d2
		return false

print dateIsBefore(2000,10,30,2010,20,20)

Algorithm Pseudocode
days = # of days in month1 - day1
month1 += 1
while month1 < month2:
    days += # of days in month1
    month1 += 1
days += day2
while year1 < year2:
    days += days in year1

#simplier
days = 0
while date1 is before date2:
    date1 = day after date1
    days += 1
return days




	

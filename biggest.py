def biggest (a,b,c):
	if a > b and a > c:
		r = a
	if b > a and b > c:
		r = b
	if c > a and c > b:
		r = c
	return r
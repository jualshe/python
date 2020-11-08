t.color(1,1,0) 
t.begin_fill() 
t.circle(50) 
t.end_fill()

def mycircle(red, green, blue): 
	t.color(red, green, blue)
	t.begin_fill() 
	t.circle(50) 
	t.end_fill()

mycircle(0, 1, 0)
mycircle(0, 0.5, 0)

mycircle(1, 0, 0)
mycircle(0.5, 0, 0)
mycircle(0, 0, 1)
mycircle(0, 0, 0.5)

mycircle(0.9, 0.75, 0)
mycircle(1, 0.7, 0.75)

mycircle(1, 0.5, 0)
mycircle(0.9, 0.5, 0.15)

mycircle(0, 0, 0)

mycircle(1, 1, 1)


def mysquare(size):
	for x in range(1, 5):
		t.forward(size) 
		t.left(90)

mysquare(50)

t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)

t.reset()
t.begin_fill()
mysquare(50)
t.end_fill()

def mysquare(size, filled): 
	if filled == True:
		t.begin_fill() 
	for x in range(1, 5): 
		t.forward(size)
		t.left(90) 
	if filled == True: 
		t.end_fill()
def octagon(size, filled):
	if filled == True:
		t.begin_fill()
	for x in range (1,9):
		t.forward(size)
		t.left(45)
	if filled == True:
		t.end_fill()


t.color(0.9, 0.75, 0.9)
octagon(80, True)
t.color(0,0,0)
octagon(80, False)
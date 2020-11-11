def octagon(size, filled):
	if filled == True:
		t.begin_fill()
	for x in range (1,9):
		t.forward(size)
		t.left(45)
	if filled == True:
		t.end_fill()
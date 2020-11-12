def draw_star(size, points):
	for x in range(1, points):
		t.forward(size) 
		if x % 2 == 0: 
			t.left(175)
		else: 
			t.left(225)
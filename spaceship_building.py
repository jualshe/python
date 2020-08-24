def spaceship_building(cans):
	total_cans = 0 
	for week in range(1,553):
		total_cans = total_cans+cans
		if total_cans >500:
			break
		print('week %s, cans: %s' % (week, total_cans))



spaceship_building(2)
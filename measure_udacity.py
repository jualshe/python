def measure_udacity(list_of_strings):
	count = 0
	for e in list_of_strings:
		if e[0] == 'U':
			count = count + 1
	return count


print measure_udacity(['Dave','Sebastian','Katy'])
print measure_udacity(['Umika','Umberto'])
print measure_udacity(['usa', 'United States', 'Umka', 'Uliana', 'enotik'])
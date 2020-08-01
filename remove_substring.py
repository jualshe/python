def remove(somestring, sub):
    """Return somestring with sub removed."""
    print"# DEBUG:"
    location = somestring.find(sub)
	if location == -1:
		return somestring
    print"# location",location
    length = len(sub)
    print " #lenght" , lenght
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    print "# before and after", part_before, part_after
    return part_before + part_after

    print
def binary_search(alist, item):
	low = 0
	high = len(alist)-1

	while low <= high:
		mid = (low + high)//2
		guess = alist[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None


print binary_search([1, 3, 5, 7, 9], 3)
print binary_search([1, 3, 5, 7, 9], -1)
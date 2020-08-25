def binary_search(alist, item):
	low = 0 #low and high keep track of which part of the list you’ll search in
	high = len(alist)-1

	while low <= high: #While you haven’t narrowed it down to one element 
		mid = (low + high)//2 #check the middle element.
		guess = alist[mid]
		if guess == item: 
			return mid #Found the item
		if guess > item: #The guess was too high
			high = mid - 1
		else: #The guess was too low
			low = mid + 1
	return None #The item doesn’t exist


print binary_search([1, 3, 5, 7, 9], 3)
print binary_search([1, 3, 5, 7, 9], -1)

#1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?
#log2 128=7 --> 2^7=128 
# 1.2 Suppose you double the size of the list. What’s the maximum number of steps now?
# 128*2=265 -->2^8


# 1-10

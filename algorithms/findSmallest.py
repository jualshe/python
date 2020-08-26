def findSmallest(arr): 
	smallest = arr[0] #Stores the smallest value
	smallest_index = 0 #Stores the index of the smallest value
		for i in range(1, len(arr)):
			if arr[i] < smallest: smallest = arr[i] smallest_index = i
	    return smallest_index
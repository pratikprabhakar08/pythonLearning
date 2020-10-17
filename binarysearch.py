#binay search
def binarySearch(arr, l, r, x): 

	while l <= r: 

		mid = l + (r - l) // 2; 
		
		# if number present at mid, return it
		if arr[mid] == x: 
			return mid 

		# If number is greater, ignore left half 
		elif arr[mid] < x: 
			l = mid + 1

		# If number is smaller, ignore right half 
		else: 
			r = mid - 1
	
	# If we reach here, then the element 
	# was not present 
	return -1

# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print ("Element is present at index % d" % result) 
else: 
	print ("Element is not present in array") 

# Python3 implementation to find length 
# of longest increasing circular subarry 

# function to find length of longest 
# increasing circular subarry 
def longlenCircularSubarr (arr, n): 
	
	# if there is only one element 
	if n == 1: 
		return 1
	
	# 'startLen' stores the length of the 
	# longest increasing subarray which 
	# starts from first element 
	startLen = 1
	
	len = 1
	max = 0
	
	# finding the length of the longest 
	# increasing subarray starting from 
	# first element 
	for i in range(1, n): 
		if arr[i - 1] < arr[i]: 
			startLen+=1
		else: 
			break
	
	if max < startLen: 
		max = startLen 
		
	# traverse the array index (i+1) 
	for j in range(i + 1, n): 
		
		# if current element if greater than 
		# previous element, then this element 
		# helps in building up the previous 
		# increasing subarray encountered 
		# so far 
		if arr[j - 1] < arr[j]: 
			len+=1
		else: 
			# check if 'max' length is less 
			# than the length of the current 
			# increasing subarray. If true, 
			# then update 'max' 
			if max < len: 
				max = len
			
			# reset 'len' to 1 as from this 
			# element again the length of the 
			# new increasing subarray is 
			# being calculated 
			len = 1
			
	# if true, then add length of the increasing 
	# subarray ending at last element with the 
	# length of the increasing subarray starting 
	# from first element - This is done for 
	# circular rotation 
	if arr[n - 1] < arr[0]: 
		len += startLen 
	print(arr)
	# check if 'max' length is less than the 
	# length of the current increasing subarray. 
	# If true, then update 'max' 
	if max < len: 
		max = len
	
	return max

# Driver code to test above 
A = [5, 4, 0, 3, 1, 6, 2] 
n = len(A) 
print("Length = ",longlenCircularSubarr(A, n)) 

# This code is contributed by "Sharad_Bhardwaj". 

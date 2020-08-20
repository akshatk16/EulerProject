def binarySearch(arr, beg, end, x):

	while beg <= end:
		mid = beg + (end - beg)//2

		if arr[mid] == x:  # found
			return True

		elif arr[mid] < x:
			beg = mid + 1

		else:
			end = mid - 1
	return False  # not found

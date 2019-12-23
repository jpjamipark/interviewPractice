def binarySearch(target, l):
	upper = len(l)-1
	lower = 0
	while(upper >= lower):
		median = (upper+lower)//2
		if(l[median] > target):
			upper = median-1
		elif(l[median] == target):
			return median
		else:
			lower = median+1
	return -1


def binarySearchLower(target, l):
	index = binarySearch(target,l)
	if(index == -1):
		return -1
	else:
		while(target == l[index] and index > 0):
			index-=1
	return index+1


print(binarySearchLower(6,[1,2,3,4,5,6,6,6,6,7,8,9]))
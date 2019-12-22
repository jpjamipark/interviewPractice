def stonks(x):
	if(x == None):
		return 0

	trough = x[0]
	profit = 0
	for i in range(len(x)):
		if(x[i] < trough):
			trough = x[i]
		if((x[i] - trough) > profit):
			profit = x[i]-trough
	print(profit)

stonks([54,3,2,1,0])

def findLongestSubarray(x):
	if(x == None):
		return 0

	recentVal = x[0]
	length = 0
	maxLength = 0

	for i in range(len(x)):
		if(recentVal == x[i]):
			length+=1
			if(length > maxLength):
				maxLength = length
		else:
			recentVal = x[i]
			length = 1
	print(maxLength)

print(findLongestSubarray([1,2,3,4,5]))
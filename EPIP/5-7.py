# O(n) size, O(n) runtime

def stonksDouble(x):
	max_profit = float('-inf')
	trough = x[0]
	peak = 0
	max_profit_one = [0]*len(x)
	max_profit_two = [0]*len(x)


	for i in range(len(x)):
		trough = min(trough, x[i])
		max_profit = max(max_profit, x[i]-trough)
		max_profit_one[i] = max_profit

	max_profit = 0
	for i in reversed(range(len(x))):
		peak = max(peak, x[i])
		max_profit = max(max_profit, peak-x[i])
		max_profit_two[i] = max_profit

	max_profit = 0
	for i in range(len(x)-1):
		max_profit = max(max_profit, max_profit_one[i]+max_profit_two[i+1])

	print(max_profit)

stonksDouble([12,11,13,9,12,8,14,13,15])

# O(1) size, O(n) runtime - TODO, not sure how to do this one. Maybe use the array itself?

def dutchFlag(x, pivotIndex):
	end = len(x)-1
	start = 0
	index = start

	pivot = x[pivotIndex]

	while(index < end):
		if(x[start] < pivot):
			start+=1
			index = start
			continue
		if(x[end] > pivot):
			end-=1
			continue
		if x[start] == pivot and x[end] < pivot:
			x[start], x[end] = x[end], x[start]
		elif x[start] > pivot and x[end] < pivot:
			x[start], x[end] = x[end], x[start]
		elif x[start] > pivot and x[end] == pivot:
			x[start], x[end] = x[end], x[start]
		elif x[start] == pivot and x[end] == pivot:
			if(x[index] == pivot):
				index+=1
			elif(x[index] < pivot):
				x[index], x[start] = x[start], x[index]
			elif(x[index] > pivot):
				x[index], x[end] = x[end], x[index]
	print(x)

def dutchFlagSinglePass(x, pivotIndex):
	end = len(x)-1
	start = 0
	index = start

	pivot = x[pivotIndex]

	while(index < end):
		if x[index] < pivot:
			x[start], x[index] = x[index], x[start]
			start+=1
			index+=1
		elif x[index] == pivot:
			index+=1
		else:
			x[index], x[end] = x[end], x[index]
			end-=1
	print(x)


def dutchFlagMultiPass(x,pivotIndex):
	pivot = x[pivotIndex]
	start = 0
	index = 0
	# shift all values lower than pivot to start of array
	while index < len(x):
		print(x)
		if x[index] < pivot:
			x[start], x[index] = x[index], x[start]
			start+=1
		index+=1

	index = len(x)-1
	end = len(x)-1
	# shift all values greater than pivot to end of array
	while index > start:
		if x[index] > pivot:
			x[index], x[end] = x[end], x[index]
			end-=1
		index-=1

	print(x)


def dutchFlagVariant(x):
	start = 0
	for i in range(len(x)):
		if(x[i] > 0):
			x[i], x[start] = x[start], x[i]
			start+=1
	print(x)



dutchFlagVariant([0,1,2,0,0,0,0,0,0,2,1])






def replaceAndRemove(x, size):
	writeIndex = 0
	a_count = 0
	for i in range(size):
		if(x[i] != "b"):
			x[writeIndex]= x[i]
			writeIndex+=1
		if(x[i] == "a"):
			a_count+=1

	currIndex = writeIndex-1
	writeIndex = writeIndex-1+a_count

	while(currIndex >= 0):
		if(x[currIndex] == "a"):
			x[writeIndex] = "d"
			x[writeIndex-1] = "d"
			writeIndex-=2
		else:
			x[writeIndex] = x[currIndex]
			writeIndex-=1
		currIndex-=1
	return x

print(replaceAndRemove(list("asfbbbbaaaa       "), 11))
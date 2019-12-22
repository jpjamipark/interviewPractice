def convertStringToInteger(x):
	val = 0



	for char in (list(x)):
		print(type(char))
		if ord(char) <= ord('9') and ord(char) >= ord('0'):
			val *= 10
			val += ord(char)-ord('0')
	if(x[0] == "-"):
		val *= -1
	return val
print(convertStringToInteger("-100000"))


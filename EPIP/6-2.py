
convert = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def decimalToBase(x, base):
	value = ""
	while(x > 0):
		value=convert[x%base]+value
		x = x//base
	return value

def baseToDecimal(x, base):

	decimal = 0
	baseVal = 1

	for char in reversed(list(x)):
		if(ord(char) <= ord('9') and ord(char) >= ord('0')):
			decimal += (ord(char)-ord('0'))*baseVal
		elif(ord(char) <= ord('F') and ord(char) >= ord('A')):
			decimal += ((ord(char)-ord('A'))+10)*baseVal
		baseVal *= base
	return decimal

print(baseToDecimal("ABCDE", 15))
print(decimalToBase(baseToDecimal("ABCDE", 15), 15))
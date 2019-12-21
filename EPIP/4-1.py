# Compute parity of bitwise word


# Brute force parity with some clever bit shifting.
def parityBruteforce(x):
	result = 0
	while(x):
		result ^= 1
		# returns x without the least significant bit
		# 1001 becomes 1000
		x&=(x-1) 
	return result

# Each XOR retains the number of bits. So you can continously XOR with itself 
# and then cache the remaining value.
parityCache = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
def parity(x):
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x &= 0xF
	return parityCache[x]



for x in range(256):
	print("Parity of",x,  "is:", parity(x))
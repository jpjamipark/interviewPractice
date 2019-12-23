class Stack:
	def __init__(self):
		self.stack = []
		self.max = []
	def push(self,x):
		self.stack.append(x)
		if(len(self.max) == 0 or self.max[-1][0] < x):
			self.max.append((x,1))
		elif(self.max[-1] == x):
			self.max[-1][1]+=1 
	def pop(self):
		if(len(self.stack) > 0):	
			if(self.max[-1][0] == self.stack[-1]):
				assert self.max[-1][1] >= 1, "Can't have negative/zero count"
				if(self.max[-1][1] == 1):
					self.max.pop()
				else:
					self.max[-1][1]-=1
			return self.stack.pop()
		else:
			return None
	def maxVal(self):
		if(len(self.max) > 0):
			return self.max[-1][0]
		else:
			return None

s = Stack()
s.push(0)
s.push(0)
s.push(0)
print(s.maxVal())
s.push(1)
print(s.maxVal())
s.pop()
print(s.maxVal())

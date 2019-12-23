import collections

class binaryNode:
	def __init__(self, data=0, lNode=None, rNode=None):
		self.data = data
		self.left = lNode
		self.right = rNode

class Queue:
	def __init__(self):
		self._data = collections.deque()
	def enqueue(self,x):
		self._data.append(x)
	def dequeue(self):
		return self._data.popleft()
	def isEmpty(self):
		return len(self._data) == 0


#    1
#  2   3
# 4 5 6 7
a = binaryNode(1)
b = binaryNode(2)
c = binaryNode(3)
d = binaryNode(4)
e = binaryNode(5)
f = binaryNode(6)
g = binaryNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

def computeDepth(x):
	q = Queue()
	depthArray = []

	q.enqueue((x,0))
	while(not q.isEmpty()):
		nodeAndDepth = q.dequeue()
		node = nodeAndDepth[0]
		depth = nodeAndDepth[1]
		if(node.left != None):
			q.enqueue((node.left, depth+1))
		if(node.right != None):
			q.enqueue((node.right, depth+1))
		while(depth >= len(depthArray)):
			depthArray.append([])
		depthArray[depth].append(node.data)

	return depthArray

print(computeDepth(a))



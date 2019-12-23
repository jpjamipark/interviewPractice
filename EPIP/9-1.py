class binaryNode:
	def __init__(self, data=0, lNode=None, rNode=None):
		self.data = data
		self.left = lNode
		self.right = rNode


def checkHeight(root):
	if(root == None):
		return 0, True

	rHeight, rBalance = checkHeight(root.right)
	lHeight, lBalance = checkHeight(root.left)

	if(rBalance and lBalance and abs(rHeight-lHeight) <= 1):
		return max(rHeight,lHeight)+1, True
	else:
		return 0, False
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
# b.right = e
# c.left = f
# c.right = g

print(checkHeight(a))
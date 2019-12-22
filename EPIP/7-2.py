class ListNode:
	def __init__(self, data = 0, next = None):
		self.data = data
		self.next = next

# def reverseSublist(x, s, f):
# 	dummy_head = sublist_head = ListNode(0,x)
# 	for _ in range(start-1):
# 		sublist_head = sublist_head.next

# 	curr = sublist_head.next
# 	for _ in range(finish-start):
# 		next = curr.next
# 		curr.next = next.next
# 		next.next = sublist_head.next
# 		sublist_head.next = future

def reverseLinkedList(x):
	prev = None
	curr = x
	nex = curr.next
	while nex != None:
		print(curr.data)
		nex = curr.next
		curr.next = prev
		prev = curr
		curr = nex
		
	return prev


list1 = ListNode()
list1.next = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
reversed = reverseLinkedList(list1)

while(reversed != None):
	print(reversed.data)
	reversed = reversed.next

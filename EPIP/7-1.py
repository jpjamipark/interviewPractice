class ListNode:
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next = next_node

def search_list(l,key):
	curr = l
	while(curr != none):
		if(curr.data == key):
			return curr
		else:
			curr = curr.next
	return None

def delete_after(node):
	node.next = node.next.next

def mergeTwoLists(list1, list2):
	dummyHead = ListNode()
	curr = dummyHead

	while(list1 != None and list2 != None):
		if(list1.data < list2.data):
			curr.next = list1
			list1 = list1.next
		elif(list1.data >= list2.data):
			curr.next = list2
			list2 = list2.next
		curr=curr.next

	if(list1 != None):
		curr.next = list1
	elif(list2 != None):
		curr.next = list2

	return dummyHead

list1 = ListNode()
list1.next = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

list2 = ListNode()
list2.next = ListNode(1, ListNode(4, ListNode(6, ListNode(7, None))))

merged = mergeTwoLists(list1, list2)

while(merged != None):
	print(merged.data)
	merged = merged.next

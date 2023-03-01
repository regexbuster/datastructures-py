class Node:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next = next_node

	def setValue(self, value):
		self.value = value

	def getValue(self):
		return self.value

	def setNext(self, next_node):
		if not isinstance(next_node, Node):
			raise TypeError(f"next_node in function setNext of class Node was set to {type(next_node)} not Node")
		self.next = next_node

	def getNext(self):
		return self.next

class LinkedList:
	def __init__(self, head=None):
		self.size = 0
		self.head = head

		if not (self.head == None):
			self.size += 1

	def insertAtEnd(self, value):
		if self.isEmpty():
			self.insertAtHead(value)
			return

		new_node = Node(value)

		current_node = self.head
		while not(current_node.next == None):
			current_node = current_node.next

		current_node.next = new_node
		self.size += 1

	def insertAtHead(self, value):
		after_head = self.head
		new_head = Node(value, after_head)

		self.head = new_head
		self.size += 1

	def delete(self, del_node_value):
		if self.head is not None and self.head.value == del_node_value:
			self.head = self.head.next

		if self.size > 1:

			previous_node = self.head
			current_node = self.head.next
			while True:
				if current_node == None:
					break

				if del_node_value == current_node.value:
					previous_node.next = current_node.next
					break

				previous_node = current_node
				current_node = current_node.next

	def deleteAtHead(self):
		if self.head == None:
			return False

		self.head = self.head.next

	def search(self, searchVal):
		if self.head == None:
			return None

		cur = head
		while True:
			if cur == None:
				break

			cur = cur.next

	def isEmpty(self):
		return not (self.size > 0)

	def print(self):
		if not (self.head == None):
			cur = self.head
			while True:
				print (cur.getValue())

				cur = cur.next
				if(cur == None):
					break
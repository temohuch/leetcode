class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

class SinglyLinkedListNode:
    def printNode(self, node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next

s = SinglyLinkedListNode()
s.printNode(a)
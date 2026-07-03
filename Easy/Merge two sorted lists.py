from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def build_list(values: list):
    tail = None
    head = None
    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    return head

class Solution:
    def mergeTwoLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        tail = None
        head = None
        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                if head is None:
                    head = list1
                    tail = list1
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    tail = list2
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next

        if head is None:
            if list1 is not None:
                printNode(list1)
            else:
                printNode(list2)

        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1

        if list2 is None:
            tail.next = list1
        else:
            tail.next = list2

        if list1 is None and list2 is None:
            return None

        printNode(head)



def printNode(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next

my_list1 = build_list([1, 2, 3, 4, 5])
my_list2 = build_list([2, 3, 4, 5])

s = Solution()
s.mergeTwoLists(my_list1, my_list2)
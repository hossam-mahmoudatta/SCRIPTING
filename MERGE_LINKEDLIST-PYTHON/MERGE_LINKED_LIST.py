# https://leetcode.com/problems/merge-two-sorted-lists/

# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insertAtBegin(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = ListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

class Solution(ListNode):
    def mergeTwoLists(self,
                                        list1: Optional[ListNode],
                                        list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
# https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        
        # if the list is null
        if not head:
            return None
        
        curr = head
        prev = None
        
        while curr is not None:
            
            # swapping the curr and prev nodes
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            
            # moving to the next node
            curr = curr.prev
            
        # if prev is None
        if prev is None:
            return head
        return prev.prev

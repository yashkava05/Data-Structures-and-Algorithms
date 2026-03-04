'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        # using the iterative approach.
        # since we cant traverse backwards in a singly linked list, we reverse the list first.
        # then we add carry(1) to the first node, and move the carry further if digits becomes double
        # we add a new node if the carry remains 1 till the end of the list.
        
        # using three pointers to flip the list
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next # saving the node before breaking the list
                curr.next = prev # reversing the pointer.
                prev = curr # moving prev one step forward.
                curr = next_node # traversing current forward
            return prev # prev is the new head
        
        # reversing the list
        head = reverse(head)
        
        # adding 1 to the head of a reversed list
        curr = head
        carry = 1
        
        while curr:
            total = curr.data + carry
            curr.data = total % 10 # storing the one's digit
            carry = total // 10
            
            # if carry become 0, break
            if carry == 0:
                break
            
            if curr.next is None and carry == 1:
                curr.next = Node(1) # adding a new node
                carry = 0
                break
            
            curr = curr.next
        
        head = reverse(head)
        
        return head
        
        
        
        
        
        
        

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # mapping from the original list to the copied node
        # filling with null : null so lookups on null pointers work.
        old_to_copy = {None : None}

        # creating all the copy nodes
        curr = head
        while curr:
            copy = Node(curr.val) # new node with the same value
            old_to_copy[curr] = copy # recording the mapping.
            curr = curr.next

        # wiring up next and random pointers using the map
        curr = head
        while curr:
            copy = old_to_copy[curr] # new node with the same value
            copy.next = old_to_copy[curr.next] # point to copy of random
            copy.random = old_to_copy[curr.random] # point to copy of random
            curr = curr.next

        # returning the copy of the head node
        return old_to_copy[head]

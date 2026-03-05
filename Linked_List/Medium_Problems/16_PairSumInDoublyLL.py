from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # using the classic two pointer approach as the linked list is already sorted.
        # using a results array to store the result.
        result = []
        
        # placing right pointer to the tail of the ll.
        right = head
        while right.next:
            right = right.next
            
        # left at the head, which is also the smallest element
        left = head
        
        
        # traversing the list and moving the pointers inwards
        while left != right and right.next != left:
            curr_sum = left.data + right.data
            
            if curr_sum == target:
                result.append([left.data, right.data])
                
                # moving the pointers inwards
                left = left.next
                right = right.prev
                
            elif curr_sum <= target:
                left = left.next # as the list is sorted ,we want a bigger sum
                
            else:
                right = right.prev
        return result
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

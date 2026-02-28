'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        # using a counter variable to keep count of the nodes
        count = 0
        
        # temp pointer to traverse, initially pointing to the head
        temp = head
        
        # traversing the linked list
        while temp is not None:
            
            count += 1
            
            temp = temp.next
            
        return count

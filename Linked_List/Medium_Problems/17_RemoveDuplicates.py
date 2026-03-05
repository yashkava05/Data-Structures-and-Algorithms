'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        curr = head
        
        while curr and curr.next:
            
            if curr.data == curr.next.data:
                # skipping the duplicate node
                curr.next = curr.next.next
                
                # fixing the prev pointer of the new next node
                if curr.next:
                    curr.next.prev = curr
            
            else:
                curr = curr.next
        
        return head

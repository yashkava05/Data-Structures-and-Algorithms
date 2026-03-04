'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # manipulating the linked list in place
        curr = head
        
        # iterating through the linked list and checking all the elements
        while curr:
            if curr.data == x:
            
            # checking if the first element is x
                if curr == head:
                    head = curr.next
                    if head:
                        head.prev = None
                
                # curr is a mid or tail node
                else:
                    curr.prev.next = curr.next
                    if curr.next:
                        curr.next.prev = curr.prev
            
            curr = curr.next
            
        return head

# https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        # using floyd's cycle detection algorithm
        slow = head
        fast = head
        
        # detecting if a cycle exists.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # when the pointers meet
            if slow == fast:
                count = 1 # var for keeping the count
                temp = slow.next # pointer for traversing the loop
                
                while temp != slow:
                    count += 1
                    temp = temp.next
                return count
                
        return 0

# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        # we can check by traversing the linked list and checking every element.
        temp = head
        
        while temp is not None:
            
            if temp.data == key:
                return True
            
            temp = temp.next
            
        return False

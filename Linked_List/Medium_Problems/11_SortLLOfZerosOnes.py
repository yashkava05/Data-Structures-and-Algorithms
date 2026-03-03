'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        # main idea is to traverse the list and make three different chains for the three elements.
        # chaining the elements to their respective chains by traversing the list.
        # linking all the chains in the end.
        if not head or not head.next:
            return head
        
        # creating three dummy nodes for three elements
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)
        
        # pointers to build each chain
        zero = zeroHead
        one = oneHead
        two = twoHead
        
        # traversing the list
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
            
        # connecting the three chains
        zero.next = oneHead.next if oneHead.next else twoHead.next
        
        # 1's chain points to the start of two's
        one.next = twoHead.next
        
        # terminating the final chain
        two.next = None
        
        return zeroHead.next
            
            

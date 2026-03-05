# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        # finding the length and getting a pointer to the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head
        
        curr = head
        for i in range(length - k - 1):
            curr = curr.next

        # re-linking the list
        new_head = curr.next # node after curr is the new head
        curr.next = None # breaking the list, curr is now the new head
        tail.next = head # connecting old tail to old head

        return new_head

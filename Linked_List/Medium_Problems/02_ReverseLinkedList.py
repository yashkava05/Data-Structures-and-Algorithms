# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using two pointers to keep track
        curr = head
        prev = None

        # traversing curr in the LL
        while curr:

            # saving the link between the curr and next elem
            temp = curr.next

            # reversing the list
            curr.next = prev
            # the old prev pointer is equated with the curr pointer
            prev = curr
            # and curr is pointing to temp, which moves forward.
            curr = temp
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # moving right so that gap between right and left is exactly n
        while n > 0:
            right = right.next
            n -= 1

        # when right reaches the end, left will pointing to the nth position from the end.
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

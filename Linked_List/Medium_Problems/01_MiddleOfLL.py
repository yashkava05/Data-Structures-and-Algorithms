# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using the tortoise and hare algorithm
        slow = head
        fast = head

        while fast and fast.next and slow:
            # fast moves two steps at a time
            fast = fast.next.next
            # slow moves one step at a time
            slow = slow.next

        return slow

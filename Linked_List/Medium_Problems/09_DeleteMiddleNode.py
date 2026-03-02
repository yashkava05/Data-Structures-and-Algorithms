# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using slow and fast pointers.
        if not head.next:
            return None
        # using a dummy node so slow ends at mid - 1
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # skipping the middle node's connection.
        slow.next = slow.next.next

        return head

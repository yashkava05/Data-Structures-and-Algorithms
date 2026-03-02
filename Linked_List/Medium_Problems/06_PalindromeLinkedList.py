# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # using fast and slow pointers to find the optimal approach
        # finding the middle element first
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # after the pointers meet, we will be on the middle element

        # reversing the second half of the LL.
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev # so that the link doesnt break
            prev = curr
            curr = nxt
            # we have now reversed the linked list

        # comparing both the halves.
        left = head
        right = prev # prev is the head of the reversed second half

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

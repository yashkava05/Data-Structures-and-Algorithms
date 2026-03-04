# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy for acting as a fake head
        dummy = ListNode()
        curr = dummy
        carry = 0 # tracking the carry from the previous addition

        # iterating until both the lists are not empty or the leftover is not empty
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0


            # adding both digits plus the carry if any
            val = v1 + v2 + carry

            # if val is >= 10, carry = 1 otherwise carry is 0
            carry = val // 10

            # actual digit is the one's place
            val = val % 10

            curr.next = ListNode(val)

            # moving the current pointer forward
            curr = curr.next

            # advancing l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

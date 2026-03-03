# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # using two pointers
        l1 = headA
        l2 = headB

        # moving both pointers until they point to the same node
        while l1 != l2:
            # moving to the next node, else switching the list
            l1 = l1.next if l1 else headB

            l2 = l2.next if l2 else headA

        return l1

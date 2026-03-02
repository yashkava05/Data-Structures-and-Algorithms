# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head # odd starts at the first node
        even = odd.next # even starts at the second node
        even_head = even # to continue the link

        while even and even.next:
            # linking current odd node to the next odd
            odd.next = even.next
            odd = odd.next # advancing the odd pointer

            # linking current even to the next even
            even.next = odd.next
            even = even.next
        
        # connecting odd's last node to even's first node
        odd.next = even_head
        return head

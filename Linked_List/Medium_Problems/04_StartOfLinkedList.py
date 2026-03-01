# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using tortoise and hare method.
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # when they meet in the cycle
            if slow == fast:
                # pointing slow back to the original position.
                slow = head

                # they will again meet at the start of the cycle because of the distance travelled by fast.
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None

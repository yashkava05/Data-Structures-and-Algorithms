# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using a set to keep a track of all elements in the linked lists
        seen = set()

        curr = head
        # traversing and checking whether or not the element is in the set.
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

# Optimal Approach
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # optimal - using fast and slow pointers, flyods algorithm
        slow = head
        fast = head

        # traversing till the end of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # both pointers will meet if there's a cycle.
            if fast == slow:
                return True
        return False

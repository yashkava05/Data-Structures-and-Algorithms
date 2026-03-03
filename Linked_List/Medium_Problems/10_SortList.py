# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using merge sort to divide the list into smaller halves and then bringing all the halves together to merge them again.
        # if the list is empty or only consists of a single node
        if not head or not head.next:
            return head
        
        # step 1, finding the middle node first
        middle = self.findMiddle(head)

        # step 2, splitting the list from the middle element
        right = middle.next
        middle.next = None
        left = head

        # step 3, recursively sorting both the halves
        left = self.sortList(left)
        right = self.sortList(right)

        # step 4, merging the two sorted halves and returning
        return self.merge(left, right)
    
    # finding the middle using the tortoise and hare method.
    def findMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next # starting fast one step ahead so that slow node stops on the left side of the left center

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        # using dummy node for easy merging.
        dummy = ListNode(-1)
        curr = dummy

        # comparing nodes from both the lists and picking the smaller one.
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        
        # attaching remaining nodes from both the lists
        curr.next = list1 if list1 else list2

        return dummy.next

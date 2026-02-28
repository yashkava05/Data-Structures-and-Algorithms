# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # we cannot access the previous elements therefore, we update the current element to be deleted.
        # copying the next elem's val and deleting that instead.
        node.val = node.next.val
        node.next = node.next.next

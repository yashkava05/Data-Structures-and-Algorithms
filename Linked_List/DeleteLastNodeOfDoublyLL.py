# https://www.naukri.com/code360/problems/delete-last-node-of-a-doubly-linked-list_8160469?leftPanelTabValue=PROBLEM

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    # Write your code here
    # if the list is empty
    if not head:
        return None
    
    # if only one node is present
    if not head.next:
        return None

    # traverse to the last node
    curr = head
    while curr.next is not None:
        curr = curr.next
    
    curr.prev.next = None
    curr.prev = None

    return head
    pass

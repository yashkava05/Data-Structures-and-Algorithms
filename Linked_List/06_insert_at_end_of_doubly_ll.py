class Node:
    def __init__(self, data):
        # making the node class with next and prev pointer as Null
        self.data = data
        self.next = None
        self.prev = None
        
def insert_at_end(head, new_data):
    # creating a new node
    new_node = Node(new_data)
    
    # if LL is empty, setting the current node as the head
    if head is None:
        head = new_node
    else:
        curr = head
        # traversing to bring the current pointer to the end of the linked list
        while curr is not None:
            curr = curr.next
            
        # pointing the next pointer of the last node to the new node
        curr.next = new_node
        
        
        # pointing the prev of the last new node to the curr
        new_node.prev = curr
        
    return head

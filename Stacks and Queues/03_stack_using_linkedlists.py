# Structure of linked list Node
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.top = None

    def isEmpty(self):
        # Check if the stack is empty
        return self.top == None
        

    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        
        

    def pop(self):
        # Removes an element from the top of the stack
        if self.top == None:
            return -1
        else:
            prev = self.top
            self.top = self.top.next
        return prev.data
        


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.top == None:
            return -1
        else:
            return self.top.data


    def size(self):
        # Returns the current size of the stack
        if self.top == None:
            return 0
        temp = self.top
        count = 1
        while temp.next != None:
            temp = temp.next
            count += 1
        return count

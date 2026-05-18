# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.top = None
        

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.top == None
        

    def enqueue(self, x):
        # Add element x to the rear
        if self.top == None:
            self.top = Node(x)
        else:
            new_node = Node(x)
            temp = self.top
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        

    def dequeue(self):
        # Remove the front element
        if self.top == None:
            return -1
        else:
            prev = self.top
            self.top = self.top.next
            return prev.data
        


    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.top == None:
            return -1
        else:
            return self.top.data


    def size(self):
        # Return current size
        if self.top == None:
            return 0
        temp = self.top
        count = 1
        while temp.next != None:
            temp = temp.next
            count += 1
        return count

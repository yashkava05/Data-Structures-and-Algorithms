# Creating a linked list in python.
# node class for representing a node in the linke list
class Node:
    def __init__(self, data, next=None):
        self.data = data # the current data value
        self.next = next # pointer to the next value
        
    # Driver code
if __name__ == "__main__":
    # Create an array
    arr = [2, 5, 8, 7]

    # Create first node
    y = Node(arr[0])

    # Print memory reference of node
    print(y)

    # Print data stored in node
    print(y.data)

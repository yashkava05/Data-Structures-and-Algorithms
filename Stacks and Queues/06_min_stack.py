class MinStack:

    def __init__(self):
        self.stack = []
        # taking another stack to store the min at the moment.
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        # appending the min from the current val and the value before.
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # O(1) access to the min element at the moment.
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

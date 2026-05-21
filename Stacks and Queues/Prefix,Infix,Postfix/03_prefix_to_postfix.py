class Solution:
    def preToPost(self, s):
        stack = []
        operators = set(['+', '-', '*', '/', '%', '^'])
        
        # traversing through the given s by reversing it.
        for ch in s[::-1]:
            if ch in operators:
                
                op1 = stack.pop()
                op2 = stack.pop()
                
                # concatentating them to form the postfix string.
                postfix = op1 + op2 + ch
                
                stack.append(postfix)
                
            else:
                # if ch is an operand instead of operator.
                stack.append(ch)
                
        
        return stack[-1]

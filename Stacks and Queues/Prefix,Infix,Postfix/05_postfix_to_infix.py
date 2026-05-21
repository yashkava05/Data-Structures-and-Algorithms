#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # using a stack to store all the elements.
        stack = []
        
        # keeping all the operators in a set.
        operators = set(['+', '-', '*', '/', '%', '^'])
        
        # traversing through the postfix array.
        for ch in postfix:
            if ch in operators:
                
                op1 = stack.pop()
                op2 = stack.pop()
                
                infix = '(' + op2 + ch + op1 + ')'
                
                stack.append(infix)
                
            else:
                stack.append(ch)
                
        return stack[-1]

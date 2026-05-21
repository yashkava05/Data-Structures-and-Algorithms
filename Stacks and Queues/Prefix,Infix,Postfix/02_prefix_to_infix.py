class Solution:
    def preToInfix(self, pre_exp):
        stack = []
        
        # storing the operators in a set to identify them easily.
        operators = set(['+', '-', '*', '/', '%', '^'])
        
        # traversing the array right to left so we can get the operands first.
        for ch in pre_exp[::-1]:
            if ch in operators:
                # popping two operands from the stack.
                # concatenating them together and pushing them again.
                op1 = stack.pop()
                op2 = stack.pop()
                
                # forming the infix expression with parenthesis.
                infix = '(' + op1  + ch + op2 + ")"
                stack.append(infix)
            # else if ch is only operand pushing it directly onto the stack.
            else:
                stack.append(ch)
                
        
        return stack[-1]

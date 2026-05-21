class Solution:
    def postToPre(self, s):
        stack = []
        operators = set(['+', '-', '*', '/', '%', '^'])
        
        for ch in s:
            if ch in operators:
                
                op1 = stack.pop()
                op2 = stack.pop()
                
                prefix = ch + op2 + op1
                
                stack.append(prefix)
            
            else:
                stack.append(ch)
                
        return stack[-1]

class Solution:
    def infixtoPostfix(self, s):
        # first making a precedence function, defining all the priority levels clearly
        def prec(c):
            if c == '^':
                return 3
            elif c in ('*', '/'):
                return 2
            elif c in ('+', '-'):
                return 1
            return -1
        
        stack = []
        result = []
        
        for c in s:
            # if an operand, directly appending to the result
            if c.isalnum():
                result.append(c)
                
            # left parenthesis, pushing to operate on it.
            elif c == '(':
                stack.append(c)
            
            # pop until opening parenthesis is found.
            elif c == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop() # removing the opening parenthesis itself.
                
            else:
                while (stack and stack[-1] != '(' and 
                      (prec(stack[-1]) > prec(c) or
                      (prec(stack[-1]) == prec(c) and c != '^')
                      )):
                    result.append(stack.pop())  # ← indented as while body
                stack.append(c)
                
        # pop remaining operators.
        while stack:
            result.append(stack.pop())
            
        return ''.join(result)

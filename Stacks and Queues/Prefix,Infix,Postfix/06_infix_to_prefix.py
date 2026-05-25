class Solution:
    def infixToPrefix(self, s):
        # defining operator precedence levels.
        def precedence(op):
            if op == '^':
                return 3
            if op in ('*', '/'):
                return 2
            if op in ('+', '-'):
                return 1
            return 0
        
        def infix_to_postfix(exp):
            stack = []
            result = []
            
            for ch in exp:
                # operand directly goes to the output.
                if ch.isalnum():
                    result.append(ch)
                    
                elif ch == '(':
                    stack.append(ch)
                
                elif ch == ')':
                    while stack and stack[-1] != '(':
                        result.append(stack.pop())
                        
                    stack.pop() # removing the '('
                    
                else:
                    # popping operators with equal or higher precedence.
                    while (stack and stack[-1] != '(' and 
                    (precedence(stack[-1]) > precedence(ch) or
                    (precedence(stack[-1]) == precedence(ch) and ch == '^'))):  # ✅ flipped
                        result.append(stack.pop())
                        
                    stack.append(ch)
                    
            while stack:
                result.append(stack.pop())
                
            return ''.join(result)
                
        reversed_s = s[::-1]
        
        swapped = ''
        
        for ch in reversed_s:
            # swapping brackets so postfix algorithm works correctly.
            if ch == '(': swapped += ')'
            elif ch == ')': swapped += '('
            else: swapped += ch
            
        postfix = infix_to_postfix(swapped)
        
        return postfix[::-1]

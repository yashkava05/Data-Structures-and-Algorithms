class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # storing all the opening parenthesis in an array.
        parenthesis = ['(', '{', '[']

        # checking every char in the string.
        for c in s:
            # appending all the opening parenthesis.
            if c in parenthesis:
                stack.append(c)
            else:
                # before checking all the closing ones, checking if the stack is empty or has some elements.
                if len(stack) == 0:
                    return False
                check = stack.pop()
                if check == '(' and c == ')':
                    continue
                elif c == "}" and check == "{":
                    continue
                elif c == "]" and check == '[':
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

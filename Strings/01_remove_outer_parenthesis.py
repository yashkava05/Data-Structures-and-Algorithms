class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # using a counter to keep a track of the outer or inner parenthesis
        # we have to remove the outer most parenthesis so we increment only when it is greater than 0
        result = []

        counter = 0

        for char in s:
            if char == '(':
                counter += 1 # incrementing the counter when we encounter an opening (
                # adding to the result only if it's an inner (, meaning counter > 1
                if counter > 1:
                    result.append(char)
            
            else:
                # decrementing the counter when we encounter a closing )
                counter -= 1
                # only adding if it's an inner closing ), not the outer of a pair
                if counter > 0:
                    result.append(char)

        
        return ''.join(result)

class Solution:
    def myAtoi(self, s: str) -> int:
        # boundaries for clamping the numbers
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        # implementing the problem recursively.
        # helper function to build the number, one digit at a time
        def helper(i, num, sign):
            # if iteration has gone past the length of the string or curr char is not a digit, return the final result
            if i >= len(s) or not s[i].isdigit():
                return sign * num
            
            # shifting existing digits of the num to the left to continue making the original number
            num = num * 10 + int(s[i])

            # overflow check with the sign of the number
            if sign * num >= INT_MAX:
                return INT_MAX
            if sign * num <= INT_MIN:
                return INT_MIN

            # recursing to the next char with the updated number
            return helper(i + 1, num, sign)

        # skipping leading whitespaces
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # detecting optional sign and moving past it
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        return helper(i, 0, sign)

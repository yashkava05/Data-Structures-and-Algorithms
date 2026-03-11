class Solution:
    def myAtoi(self, s: str) -> int:
        # base case, handling empty string
        if not s:
            return 0

        n = len(s)
        index = 0 

        # skipping leading whitespaces
        while index < n and s[index] == ' ':
            index += 1
        
        # if the string only contains whitespaces
        if index == n:
            return 0
        
        # determining the sign of the number
        sign = -1 if s[index] == "-" else 1

        # traversing past the sign character
        if s[index] in ['-', '+']:
            index += 1
        
        # res var to store the result
        result = 0
        # making the overflow threshold
        overflow_thres = (2 ** 31 - 1) // 10

        # processing digits of the string
        while index < n:
            # stopping if the current char is not a digit.
            if not s[index].isdigit():
                break

            curr_digit = int(s[index])

            # checking for overflow before updating the result
            if result > overflow_thres or (result == overflow_thres and curr_digit > 7):
                return 2 ** 31 -1 if sign > 0 else -(2 ** 31)

            # updating the result
            result = result * 10 + curr_digit
            index += 1

        # applying the final sign and returning the result
        return sign * result

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # # brute force approach. 
        # # scanning all the digits from left to right
        # # removing the first digit that is greater than the leading digit.
        # # remove all remaining zeros from the result.
        # # leftmost digits carry the most value, so we are removing the peak as we traverse from left to right.
        # num = list(num)
        # # repeat until we have removed k digits
        # while k:
        #     # starting from the second digit
        #     i = 1
        #     # advancing while the digits stay increasing
        #     while i < len(num) and num[i] >= num[i - 1]:
        #         i += 1
        #     # when the loop breaks, remove the first digit
        #     num.pop(i - 1)
        #     k -= 1

        # # index for skipping leading zeros
        # i = 0
        # # advancing past every leading zero
        # while i < len(num) and num[i] == '0':
        #     i += 1
        # # dropping the leading zeros
        # num = num[i:]

        # return ''.join(num) if num else '0'

        # optimal approach - using a stack
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        while stack and k:
            stack.pop()
            k -= 1
        
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        
        res = stack[i:]

        return ''.join(res) if res else '0'

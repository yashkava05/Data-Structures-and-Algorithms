class Solution:
    def largestOddNumber(self, num: str) -> str:
        # finding the last odd digit in num to make it the largest odd digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                return num[:i + 1]
        return ""

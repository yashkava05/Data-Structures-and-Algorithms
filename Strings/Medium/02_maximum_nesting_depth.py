class Solution:
    def maxDepth(self, s: str) -> int:
        # iterating through the string once and storing the result in two variables.
        # for appending the current string.
        curr = 0
        # for taking the max between current and max count of the depth.
        res = 0

        for c in s:
            if c == '(':
                curr += 1
            elif c == ")":
                curr -= 1
            
            res = max(res, curr)

        return res

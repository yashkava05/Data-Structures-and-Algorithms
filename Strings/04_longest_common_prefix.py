class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # taking the first string as our reference
        # for storing the result
        res = ""

        # looping through the given arr of strings till the length of the first string.
        for i in range(len(strs[0])):
            for s in strs:
                # if the current char of other strings is not equal to the curr char of the first string.
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # appending the longest common prefix.
            res += strs[0][i]

        return res

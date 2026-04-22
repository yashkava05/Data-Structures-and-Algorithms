class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # mapping the characters to each number using a hash map
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        # i = current index, curStr = string built so far.
        def backtrack(i, curStr):
            # if our built string is of the same length as the input string.
            if len(curStr) == len(digits):
                # adding it to the results string.
                res.append(curStr)
                return

            # looping through every possible char of the current digit.
            for c in digitToChar[digits[i]]:
                # recursively calling the backtrack, adding c to our current letter
                backtrack(i + 1, curStr + c)

        # base case - only start the recursion if the user actually passed in any input.
        if digits:
            # starting at index 0 with an empty string
            backtrack(0, "")

        return res

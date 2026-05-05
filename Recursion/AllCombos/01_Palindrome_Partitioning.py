class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # making lists for the final res and the partitions
        res = []
        part = []

        # recursive dfs function
        def dfs(i):
            # base case, when the pointer crosses the boundary of the result.
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    # appending the palindrome to the part list.
                    part.append(s[i: j + 1])
                    # going to the next item in the list.
                    dfs(j + 1)
                    # removing the last added substring so that we can add other strings in the partition.
                    part.pop()

        dfs(0) # starting the partitioning by calling it on the first index.

        return res

    def isPalindrome(self, s, l, r):
        # using a two pointer approach to check and compare if both the items are equal
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

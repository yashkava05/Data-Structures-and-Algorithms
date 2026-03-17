class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = "" # stores the longest palindrome found so far
        resLen = 0 # length of the longest palindrome found

        # trying every current index as the possible center of the palindrome.
        for i in range(n):
            # odd length palindrome, where the center is one character
            left = i
            right = i
            # looping while in bounds and the characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # checking if current palindrome is bigger than our best
                if (right - left + 1) > resLen:
                    res = s[left:right + 1] # update result substring
                    resLen = right - left + 1 # update res length
                left -= 1
                right += 1

            # even lenght palindromes, where two characters are at the center
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1)  > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1

                left -= 1
                right += 1

        return res

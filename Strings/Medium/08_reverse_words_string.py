class Solution:
    def reverseWords(self, s: str) -> str:
        # storing the words as individual items in a list
        words = s.split()
        # reversing the list in place using python's built in methods
        words.reverse()
        # joining all the words together
        result = " ".join(words)
        return result

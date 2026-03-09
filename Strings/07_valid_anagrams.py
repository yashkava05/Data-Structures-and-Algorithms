class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # checking the base condition, the lengths of both the strings should be the same.
        if len(s) != len(t):
            return False

        # sorting both the string alphabetically then checking them.
        return sorted(s) == sorted(t)
        

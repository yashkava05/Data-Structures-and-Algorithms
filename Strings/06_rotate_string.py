class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # adding the original string to itself to concatenate it.
        if len(s) != len(goal):
            return False

        double_s = s + s

        # checking if goal is in the doubled string
        return goal in double_s

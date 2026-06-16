class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # optimal approach using a stack.
        n = len(heights)
        max_area = 0
        stack = []

        # looping though the given array.
        for i in range(n + 1):
            # storing the current value in a var
            curr = heights[i] if i < n else 0
            # going until the current bar ends the taller ones
            while stack and heights[stack[-1]] >= curr:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)
        
        return max_area

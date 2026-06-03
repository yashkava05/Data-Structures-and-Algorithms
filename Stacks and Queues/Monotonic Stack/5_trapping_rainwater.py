class Solution:
    def trap(self, height: List[int]) -> int:
        # using a stack to store the indices of the bars
        stack = []
        water = 0

        # traversing the bars
        for i in range(len(height)):
            # traversing till we find a bigger elem than the top of the stack.
            while stack and height[i] > height[stack[-1]]:

                # popping the top elem, this is the new floor.
                floor_index = stack.pop()
                floor_height = height[floor_index]

                # the curr top will become the left wall
                # if empty, skip
                if not stack:
                    break

                # new top is the left wall
                left_index = stack[-1]
                left_height = height[left_index]

                # current bar is the right index
                right_height = height[i]

                # water level is capped by the shorter of the two walls
                water_level = min(left_height, right_height)

                width = i - left_index - 1

                # the exact water level
                water += (water_level - floor_height) * width

            stack.append(i)

        return water

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # result array to store the next greater element
        results = [-1] * n
        # stack to hold the elements
        stack = []

        # looping through 2n indices to mimic circular behaviour.
        for i in range(2 * n):
            # using modulo to wrap around indices.
            current = nums[i % n]

            while stack and current > nums[stack[-1]]:
                idx = stack.pop()
                results[idx] = current

            if i < n:
                stack.append(i)

        return results

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # optimal approach.
        n = len(nums)
        # sorting the array first
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            # taking left and right pointers from the 1th element and the n-1tj element
            left = i+1
            right = n-1
            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

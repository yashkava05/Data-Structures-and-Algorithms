class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # using binary search.
        # we focus on eliminating a half of the array, but over here, the greater element can be on any side of the mid.

        n = len(nums)
        left = 0
        right = n - 1

        while left  <= right:
            mid = left + ((right - left) // 2)

            # we will go in the direction where the element greater than mid resides.
            # and eliminate the other half
            # making sure mid isnt the first element.
            # if mid is greater than going to the left.
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # if the right neighbor is greater, going to the right subarray.
            elif mid < n - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid

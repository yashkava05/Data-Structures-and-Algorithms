class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using standard BS. 
        n = len(nums)
        low = 0
        high = n - 1
        ans = float('inf')

        # traversing while low pointer is less than/equal to high
        while low <= high:
            mid = (low + high) // 2

            # the main idea is to check which half of the array is sorted.
            # checking if the left half is sorted.
            if nums[low] <= nums[mid]:
                # taking the minimum element from the left half and eliminating the half.
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                # right is sorted, which means that the rotation point is in the left half.
                high = mid - 1
                ans = min(ans, nums[mid])
        return ans

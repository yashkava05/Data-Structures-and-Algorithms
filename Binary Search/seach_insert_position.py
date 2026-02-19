class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n-1

        while low <= high:
            mid = (low+high) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                # the low will automatically point to the next position where the mid should be inserted.
                low = mid + 1
            else:
                high = mid -1
        return low

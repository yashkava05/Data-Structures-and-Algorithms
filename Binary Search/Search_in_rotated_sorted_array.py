class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # checking if the left part of the array is sorted
            if nums[low] <= nums[mid]:

                # checking if the target lies in the left half
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1 # going to the left bound of the array
                else:
                    low = mid + 1 # going to the right
            
            else:
                # checking if target lies in the right half
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

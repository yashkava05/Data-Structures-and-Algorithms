# This is the basic problem on binary search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # we take two pointers low on the first element of the array.
        # high on the last element of the array.
        low = 0
        high = n - 1

        # we traverse the array until both the pointers meet.
        while low <= high:
            mid = (low + high) // 2 # calculating the mid element of the array.

            # checking if the mid element is equal to the target, if not changing the pointers accordingly.
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low += 1
            else:
                high -= 1
        
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # similar to rotated sorted array 1
        # using a modified binary search for this.

        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:

            # calculating the middle point element.
            mid = (low + high) // 2

            # best case, if it's equal to the target we are looking for.
            if nums[mid] == target:
                return True

            # we are also given duplicates.
            # possibility we cannot determine which halves are sorted because of duplicate elements.
            if nums[low] == nums[mid] == nums[high]:
                # shrinking the search space.
                low += 1
                high -= 1
                continue

            # if the left half is sorted, low <= mid.
            if nums[low] <= nums[mid]:
                # checking if the target actually falls in the left half.
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                # if not, going to the right half.
                else:
                    low = mid + 1
            else:
                # confirming if target lies in the right half.
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                # if not going to the left.
                else:
                    high = mid - 1
        return False

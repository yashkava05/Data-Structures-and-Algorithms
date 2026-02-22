class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        # if only one element is in the array
        if n == 1:
            return nums[0]

        # cases where there should be pairs, but if not then the elem is unique.
        # if the first elem is unique
        if nums[0] != nums[1]:
            return nums[0]

        # if last elem is unique
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        # coming to binary search.
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            # best case if the mid elem is the unique elem:
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # checking against standard index numbering if there was no unique element.
            # checking if the mid elem is the right element in the pair.
            # or : checking if the mid elem is odd element of the pair.
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                # moving to the right:
                low = mid + 1
            else:
                # if the normal indexes dont align, the unique element must be to the left.
                high = mid - 1
            
        return -1

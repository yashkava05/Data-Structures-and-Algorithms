class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # using a two biased approach for finding both the elements
        n = len(nums)
        def findfirst(nums: List[int], target: int) -> int:
            low = 0
            high = n - 1

            first = -1 # to store the potential elements
            
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    first = mid
                    # going to the left part of the array after finding the first potential element.
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def findlast(nums: List[int], target: int) -> int:
            low = 0
            high = n - 1

            last = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    last = mid
                    # going to the right of mid to find potential last index of the given target.
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = low + 1
            return last

        firstocc = findfirst(nums, target)

        lastocc = findlast(nums, target)

        return [firstocc, lastocc]

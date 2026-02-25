class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # if k is greater than number of elements in nums
        if k > n:
            return -1

        # binary range.
        low = max(nums) # the minimum would be when a single largest number is a subarray.
        high = sum(nums) # max can be the sum of all numbers in the given arr nums.

        result = high # var to store our results.

        while low <= high:
            
            # each subarray's sum should be at-most mid, if not, we move to the next subaray and expand the subarray.
            mid = (low + high) // 2

            # checking if it's possible to allocate all nums in k subarrays,
            # such that no arr contains more than mid total number of sum.
            if self.is_feasible(nums, k, mid):
                
                # mid works, saving it and finding a potentially smaller answer.
                result = mid
                high = mid - 1

            # else mid is too small to accomate the sum of all numbers in k subarrays.
            else:
                # we want a potentially larger mid, to accomate the sum in k subarrays.
                low = mid + 1
        
        return result

    # feasibility function which checks if it's possible to allocate the sum of all numbers into k subarrays such that every subarray contains at most mid number of elements.
    def is_feasible(self, nums, k, max_sum):

        # starting with the first array.
        arr = 1

        # running sum of pages for the current array.
        current_sum = 0

        # going through each element from left to right.
        for num in nums:
            # trying to give the sum to the current student.
            if current_sum + num > max_sum:

                # current array is greater than max_sum(mid), so assigning it to a new subarray.
                arr += 1
                current_sum = num

                # if already crossed k arrays, not possible.
                if arr > k:
                    return False
                
            else:
                # current subarray can take this number
                current_sum += num
        
        # if done <= k subarrays, it's feasbile
        return True

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #optimal solution using kadane's algorithm.
        #we use two variables maxi - to keep track of the maximum sum currently available
        #sum1 - to keeo track of the sum till the element we have iterated over.
        n = len(nums)
        maxi = float(-inf)

        sum1 = 0

        for i in range(n):
            sum1 += nums[i]

            if sum1 > maxi:
                maxi = max(maxi, sum1)

            if sum1 < 0:
                sum1 = 0
        
        return maxi

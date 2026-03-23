#User function Template for python3

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        # Code here
        def solve(index, current_sum):
            # if subsequence equals the current sum
            if current_sum == K:
                return True
            
            # if the length of the arr traverses or current sum becomes greater than the target
            if index == N or current_sum > K:
                return False
                
            
            # including the current element
            if solve(index + 1, current_sum + arr[index]):
                return True
            
            # excluding the current element
            if solve(index + 1, current_sum):
                return True
                
            
            return False
            
        # returing the final result
        return solve(0, 0)
            

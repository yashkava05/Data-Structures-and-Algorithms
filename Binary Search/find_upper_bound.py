# https://www.geeksforgeeks.org/problems/implement-upper-bound/1

class Solution:
    def upperBound(self, arr, target):
        # code here
        # upper bound is the element which is just greater than the given target.
        n = len(arr)
        
        low = 0
        high = n-1
        ans = len(arr)
        
        while low <= high:
            mid = (low + high) // 2
            
            # taking only the element which is greater than the target.
            if arr[mid] > target:
                ans = mid # storing the element which is just greater.
                high = mid-1
            else:
                low = mid+1
        return ans

# problem link https://www.geeksforgeeks.org/problems/implement-lower-bound/1

class Solution:
    def lowerBound(self, arr, target):
        n = len(arr)
        
        low = 0
        high = n - 1
        ans = len(arr)
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

# Link - https://www.geeksforgeeks.org/problems/rotation4723/1

class Solution:
    def findKRotation(self, arr):
        # the problem is the same as finding the minimum element of the arr.
        # bec it will the point of rotation of the arr, and by returning it's
        # index, we can get the rotation count of the array.
        n = len(arr)
        
        low = 0
        high = n - 1
        index = 0
        
        ans = float('inf')
        
        while low <= high:
            
            mid = (low + high) // 2
            
            # checking if the left half of the array is sorted.
            if arr[low] <= arr[mid]:
                # check to update the min index
                if arr[low] < ans:
                    index = low
                # the min could be in the left half, so taking it and eliminating the left half.
                ans = min(ans, arr[low])
                low = mid + 1 # shifting to the right.
            
            # else checking if the right portion is sorted.
            else:
                if arr[mid] < ans:
                    index = mid
                ans = min(ans, arr[mid])
                # going to the left half to check the rotation point.
                high = mid - 1
        return index

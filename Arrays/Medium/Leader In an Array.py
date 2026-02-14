https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

class Solution:
    def leaders(self, arr):
        #Brute force
        #Using two pointers, one for the current element
        #Second for traversing the other elements and comparing with the current element
        #ans array for storing the leaders
        ans = []
        n = len(arr)
        #iterating through each element
        for i in range(n):
            leader = True
            
            for j in range(i+1, n):
                if nums[j] >= nums[i]:
                    leader = False
                    break
            
            if leader:
                ans.append(nums[i])
                
        return ans

class Solution:
    def leaders(self, arr):
        #Storing the last element in the ans array as it's always a leader.
        #Taking a variable max to check the current leader and the current element.
        #We start traversing from the end of the given arr.
        
        n = len(arr)
        ans = []
        
        if not arr:
            return ans
        
        max_elem = arr[-1]
        ans.append(arr[-1])
        
        for i in range(n-2, -1, -1):
            if arr[i] >= max_elem:
                ans.append(arr[i])
                max_elem = arr[i]
                
        #reverse to match the order of the original arr.
        ans.reverse()
        
        return ans

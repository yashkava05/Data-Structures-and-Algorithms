# https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

class Solution:
    def minTime (self, arr, k):
        # code here
        n = len(arr)
        
        # if more painters than boards, not possible
        if k > n:
            return -1
            
        low = max(arr)
        high = sum(arr)
        
        # result var to store the final answer.
        result = high
        
        while low <= high:
            
            mid = (low + high) // 2
            
            # checking if we can allot at most mid number of boards to k painters.
            if self.is_feasible(arr, k, mid):
                
                # storing the potential result
                result = mid
                
                # trying to find an even smaller maximum
                high = mid - 1
            else:
                # else if the mid is too small, painters exceed k, we need to give more time per painter.
                low = mid + 1
        return result
        
    # greedy check to see if we can allot all boards to k painters where each painter doesnt take more than mid time.
    def is_feasible(self, arr, k, max_boards):
        # starting with the first painter
        painters = 1
        
        # running sum of board lengths for current painter
        current_sum = 0
        
        # going through each board from left to right.
        for length in arr:
            # trying to give this board to the current painter
            if current_sum + length > max_boards:
                # current painter would not be able to take this board, as it exceeds max_boards
                # so assigning to a new painter
                painters += 1
                
                current_sum = length
                
                # if we have crossed k number of painters,
                if painters > k:
                    return False
                    
            else:
                current_sum += length
                    
        return True # if we managed in less than or equal to k painters.
    
    
    
    
    

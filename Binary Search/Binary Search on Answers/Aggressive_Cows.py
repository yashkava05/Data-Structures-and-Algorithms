# https://www.geeksforgeeks.org/problems/aggressive-cows/1
class Solution:
    
    def isValid(self, stalls, cows, min_distance):
            total_stalls = len(stalls)
            cows_placed = 1 # placing first cow at stall[0]
            last_placed_index = 0
            
            for current_index in range(1, total_stalls):
                # if gap from last placed cow > min distance, place next cow
                if stalls[current_index] - stalls[last_placed_index] >= min_distance:
                    cows_placed += 1
                    last_placed_index = current_index
                    if cows_placed == cows:
                        return True
            return cows_placed == cows
    
    def aggressiveCows(self, stalls, k):
        
        # sorting the given array first.
        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0] # max possible distance
        max_min_distance = -1 # ans var
        
        # bs on answer
        while low <= high:
            mid = (low + high) // 2
            # can we place k cows with mid gaps?
            if self.isValid(stalls, k, mid):
                max_min_distance = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return max_min_distance

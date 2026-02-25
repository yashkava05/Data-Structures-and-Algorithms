# https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        n = len(stations)
        
        low = 0 # no gap between stations
        high = 0 # highest gap between consecutive stations.
        
        for i in range(1, n):
            high = max(high, stations[i] - stations[i-1])
            
        
        # BS on the answer.
        # since ans is a decimal, we keep going until preicision is met.
        while high - low > 1e-6:
            
            # mid is the max allowed gap.
            mid = (low + high) / 2
            
            if self.is_feasible(stations, k, mid):
                # mid works, trying a smaller answer.
                high = mid
            else:
                # mid is small, try to allow larger gaps.
                low = mid
                
        return high
        
    # checking how many stations do we need to make all gaps <= mid
    def is_feasible(self, arr, k, max_dist):
        
        # counting new stations needed.
        stations_needed = 0
        
        # checking gap between consecutive stations.
        for i in range(1, len(arr)):
            
            # current gap between consecutive stations.
            gap = arr[i] - arr[i - 1]
            
            # if gap is already <= max_dist, no stations needed.
            # if gap > max_dist, we need to split it.
            # no of pieces = ceil(gap, max_dist)
            # no of stations = pieces - 1
            if gap > max_dist:
                import math
                stations_needed += math.ceil(gap / max_dist) - 1
                
        # feasible if we used less than k stations.
        return stations_needed <= k
        
    
    
    
    

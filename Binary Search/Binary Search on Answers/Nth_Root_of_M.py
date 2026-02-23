# Link - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

class Solution:
    def nthRoot(self, n, m):
        left = 0
        right = m
        
        while left <=  right:
            mid = (left + right) // 2
            
            ans = 1
            
            # mutltiplying the mid n times to check if it equals m.
            for _ in range(n):
                ans = ans * mid
                if ans > m:
                    break
                
            if ans == m:
                return mid
                
            if ans < m:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

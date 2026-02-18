class Solution:
    def subarrayXor(self, arr, k):
        n = len(arr)
        # brute computing every xor using two loops
        count = 0
        
        # traversing all starting points
        for i in range(n):
            xorVal = 0
            for j in range(i, n):
                xorVal ^= arr[j]
                if xorVal == k:
                    count += 1
        
        return count

# optimal approach
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        # freq of prefix xor's
        freq = {0:1}
        
        #current prefix xor
        prefixXor = 0
        # answer count
        count = 0
        
        # traverse the array
        for num in arr:
            prefixXor ^= num
            
            # computing required xor
            target = prefixXor ^ k
            
            if target in freq:
                count += freq[target]
                
            freq[prefixXor] = freq.get(prefixXor, 0) + 1
            
        return count

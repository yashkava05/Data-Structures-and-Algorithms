class Solution:
    def subsetSums(self, arr):
        # problem based on classic decision tree problems, where we have to choose
        # between picking or not picking an element.
        # taking a results arr.
        res = []
        
        # using a recursive function which goes depth first to search for elements
        def dfs(i, cursum):
            # base case1 - we have reached the end of the array while picking or skipping elements
            if i == len(arr):
                res.append(cursum)
                return
            
            # decision 1 - picking the curr element
            # we add the curr element to our sum and move to the next element
            dfs(i + 1, cursum + arr[i])
            
            # decision 2 - not picking the curr element
            # moving to the next element in our decision tree.
            dfs(i + 1, cursum)
            
        
        dfs(0, 0)
        
        
        return res

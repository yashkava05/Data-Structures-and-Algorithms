#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
	    # res var to store all the substrings
	    result = []
	    
	    # recursive function
	    # takes the current index and the current char, which is used to decide to keep in or not
	    def solve(index, current):
	        # base case, if we reached the end of the string.
	        if index == len(s):
	            if current: # if current subsequence is empty
	                result.append(current)
	            return
	        
	        # including the current char in the substring
	        solve(index + 1, current + s[index])
	        
	        # skipping the current char from the string
	        solve(index + 1, current)
	        
	   
	    solve(0, "")
	   
	   # returning lexicographically
	    result.sort()
	   
	   
	    return result

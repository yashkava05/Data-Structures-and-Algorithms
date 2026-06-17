class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using a list to store the outputs
        output = []
        q = deque()
        left = right = 0

        while right < len(nums):
            # removing indices whose values will be smaller than the current value to be inserted
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            # adding the new index to the queue
            q.append(right)

            # front index outside the window
            if left > q[0]:
                q.popleft()
            
            # right index also outside the window
            if (right + 1) >= k:
                output.append(nums[q[0]]) # the first value is always the greatest
                left += 1
            
            right += 1
        
        return output
            

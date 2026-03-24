class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # var to store the results
        res = []

        # using a recursive function which takes the current list of elements, total of the current list and an index
        def dfs(i, cur, total):
            # if total == target
            if total == target:
                res.append(cur.copy()) # because cur list will be modified further
                return
            
            # if out of bounds or total > target
            if i >= len(nums) or total > target:
                return

            # including the current number and staying at the same index
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # skipping the current number and moving to the next index
            cur.pop() # removing what we just added
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

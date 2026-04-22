class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # another problem of the decision tree set
        nums.sort()
        res = []

        def dfs(i, cur):
            # we have made a decision for every element
            if i == len(nums):
                res.append(cur.copy())
                return

            # picking the current number
            cur.append(nums[i])
            dfs(i + 1, cur)

            # skipping the current number
            cur.pop()

            # if we already picked the current number earlier, we can skip it and move forward.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, cur)


        dfs(0, [])
        return res

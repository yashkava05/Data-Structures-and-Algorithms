class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # taking a global varable result
        # also sorting the candidates to avoid duplicate issues entirely
        candidates.sort()
        res = []

        # defining a recursive function depth first search to go to the depths of the tree
        def dfs(i, cur, total):
            # bc1 - when the total is equal to the target
            if total == target:
                res.append(cur.copy())
                return
            # bc2 - when the traversal exceeds the limit
            if i >= len(candidates) or total > target:
                return

            # making the decision in the tree.
            # including the current number
            cur.append(candidates[i])
            # traversing ahead as we cannot use the same number twice
            dfs(i + 1, cur, total + candidates[i])

            # skipping the current number
            cur.pop()

            # if we skip the current number, we must also skip the next duplicate number
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # making the recursive call with the next unique number
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res

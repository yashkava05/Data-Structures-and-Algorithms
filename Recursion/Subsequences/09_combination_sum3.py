class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # another twist of the decision tree problems. 
        # here we have an additional base case where the numbers used should be k and the total should equal to n.
        res = []

        # using a recursive depth first search function which decides to take or skip the current element.
        # i is the actual number from 1 to 9.
        def dfs(i, cur, total):
            # base case1 - when total equals target:
            if total == n and len(cur) == k:
                # appending a copy of the current array.
                res.append(cur.copy())
                return
            
            # base case2 - when we are out of bounds in different conditions.
            if len(cur) > k or total > n or i > 9:
                return

            # decision1 - picking the current number i
            cur.append(i)
            # going to the next recursive call using the number.
            # also adding i to the sum.
            dfs(i + 1, cur, total + i)

            # decision2 - skipping the current number.
            cur.pop()
            # going to the next recursive call using the next number and skipping adding the number to the sum of total.
            dfs(i + 1, cur, total)

        # making the first recursive call.
        dfs(1, [], 0)

        return res

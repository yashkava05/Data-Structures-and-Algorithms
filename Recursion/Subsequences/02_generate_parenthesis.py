class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # key concept, only adding opening parenthesis when openN < n 
        # only adding closing when closing < opening
        # valid if open == closed == n

        # using a stack to perform operations
        stack = []
        # results var
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # last element pops from here after closedN also becomes n
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

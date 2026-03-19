class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # recursive function to count valid strings starting from i
        def f(i):
            # base case, we have filled all valid strings, that means we formed one valid string
            if i == n:
                return 1

            # if index is even th index, we have 5 choices.
            if i % 2 == 0:
                # for each choice multiply with remaining ways of positions
                return (5 * f(i + 1)) % MOD
            # else if the index is odd,
            else:
                return (4 * f(i + 1)) % MOD

        return f(0)

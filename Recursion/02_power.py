class Solution:
    def myPow(self, x: float, n: int) -> float:
        # solving this by using the powers of exponents.
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            # recursing with x squared and n halved.
            res = helper(x * x, n // 2)

            # mutlipying one x again if n was odd, because it was lost while halving.
            return x * res if n % 2 else res


        # recursively calling the function.
        res = helper(x, abs(n))

        # return the result if x is positive else the reciprocal.
        return res if n >= 0 else 1 / res

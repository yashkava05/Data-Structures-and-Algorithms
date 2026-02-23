class Solution:
    def mySqrt(self, x: int) -> int:
        # handling smaller values, as sqrt will be equal to the number itself
        if x < 2:
            return x

        left = 0
        right = x // 2 # any integer's number's sqrt will always be less than half its value
        ans = 0 # to store the potential answer

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                ans = mid # could be the potential sqrt

                # moving to the right to find a closer answer.
                left = mid + 1
            else:
                right = mid - 1

        return ans

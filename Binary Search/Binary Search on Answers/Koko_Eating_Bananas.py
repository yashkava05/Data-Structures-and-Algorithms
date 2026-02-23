class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # using binary search.
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            # calculating the k value(min hours)
            k = (left + right) // 2

            hours = 0

            # calculating the total hours required using each mid value.
            for p in piles:
                hours += math.ceil(p / k)

            # if calculated hours are less than given h, we can go the left.
            if hours <= h:
                # taking the minimum hours
                res = min(res, k)
                right = k - 1
            # else going to the right.
            else:
                left = k + 1
        return res

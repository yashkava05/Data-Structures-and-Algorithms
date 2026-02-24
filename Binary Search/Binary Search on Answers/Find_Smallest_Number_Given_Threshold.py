class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2

            # calculating the sum of each ceiling.
            total = sum(math.ceil(x / mid) for x in nums)

            if total <= threshold:
                # sum is within the threshold, trying a smaller divisor
                high = mid - 1
            else:
                # sum is more than the threshold, need a bigger divisor.
                low = mid + 1

        return low

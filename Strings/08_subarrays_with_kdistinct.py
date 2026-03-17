class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) > k:
                    break

                if len(seen) == k:
                    res += 1

        return res

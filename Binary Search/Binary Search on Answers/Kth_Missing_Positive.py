class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # using binary search
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            # taking the mid point.
            mid = (low + high) // 2

            # calculating the number of missing numbers before arr[mid]
            missing = arr[mid] - (mid + 1)

            # if the missing numbers are less than k, we move right.
            if missing < k:
                low = mid + 1

            # if the missing numbers are more than k, we move left
            else:
                high = mid - 1
            
            # now high will point to the last index which is less than k.
        return k + high + 1

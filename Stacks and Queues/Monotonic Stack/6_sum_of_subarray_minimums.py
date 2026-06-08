class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        # brute force approach
        # using two loops, first to take the starting point of an array
        # second to take the ending index of the array.
        n = len(arr)
        res = 0
        MOD = 1000000007

        for i in range(n):
            min_val = arr[i]
            for j in range(i, n):
                min_val = min(min_val, arr[j])
                res = (res + min_val) % MOD

        return res """

        MOD = 10**9 + 7

        n = len(arr)
        # var to store the final result
        result = 0

        # stack for storing indices and maintaining an ascending order of the values.
        stack = []

        # traversing through the arr till the end
        for i in range(n + 1):
            curr = arr[i] if i < n else float('-inf')

            # checking if the stack has elements
            # and popping whenever the curr element breaks the ascending order
            while stack and arr[stack[-1]] >= curr:
                # popping the top of the stack
                mid = stack.pop()

                # all elements of the left will be smaller in the stack
                left = stack[-1] if stack else -1
                right = i

                left_count = mid - left
                right_count = right - mid

                result += arr[mid] * left_count * right_count
                result %= MOD

            stack.append(i)

        return result

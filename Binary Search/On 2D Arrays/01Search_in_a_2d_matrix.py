class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using standard binary seach
        # treating the matrix as a single sorted array.
        ROWS = len(matrix)
        COLS = len(matrix[0])

        left = 0
        right = ROWS * COLS - 1

        while left <= right:
            # calcualting the mid
            mid = left + (right - left) // 2

            # converting the rows and cols back to their original index.
            row = mid // COLS
            col = mid % COLS

            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False

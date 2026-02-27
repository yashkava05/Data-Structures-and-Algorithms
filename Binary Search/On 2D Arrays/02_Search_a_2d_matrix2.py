class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) # total number of rows

        # going to each row in the matrix
        for row in matrix:
            left = 0
            right = n - 1

            # parsing each element of the matrix
            while left <= right:
                mid = (left + right) // 2

                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return False

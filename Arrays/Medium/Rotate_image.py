class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # traversing through the matrix and transposing it
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reversing each row to get the desired result
        for i in range(n):
            # this simulates clockwise rotation
            matrix[i].reverse()

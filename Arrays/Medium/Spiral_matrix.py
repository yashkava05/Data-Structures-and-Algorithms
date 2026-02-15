class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # using pointers to be aware of the boundaries of the matrix
        result = []
        left = 0 # top leftmost element of the array
        right = len(matrix[0]) # right most element of the array + 1

        top = 0 #same as the leftmost initially
        bottom = len(matrix) # bottom element +1

        while left < right and top < bottom:
            # for every i in the top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            # for every i in the right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if not(left < right and top < bottom):
                break
            # for every elem in the bottom row going from right to left
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1
            # every elem in the left col from bottom to top
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left += 1
        
        return result

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left = 0
        right = len(mat) - 1

        while left < right:
            mid = (left + right) // 2

            # going to the middle col and then finding the max element from that col.
            max_col = mat[mid].index(max(mat[mid]))

            # only checking if it is greater than the element below it.
            if mat[mid][max_col] > mat[mid + 1][max_col]:
                right = mid # if peak is in the upper half.
            else:
                left = mid + 1 # peak is in the lower half.

        # when left == right, we have found the peak row.
        # max of this row is the peak element.
        peak_col = mat[left].index(max(mat[left]))
        return [left, peak_col]

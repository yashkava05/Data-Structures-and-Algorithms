class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # We add one zero to the start of the row and one to the end
        res = [[1]]

        # since we already took the first row into consideration
        for i in range(numRows - 1):
            # adding zeros before and after the original row for easy computation.
            # using a temporary array for this purpose
            temp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)

        return res

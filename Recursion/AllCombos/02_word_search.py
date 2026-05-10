class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # first storing the number of rows and cols in the cell
        rows = len(board)
        cols = len(board[0])

        # a set to track all of our chars in our path
        path = set()

        # recursive depth first search function which tracks the rows, cols and the current index at which our function is in.
        def dfs(r, c, i):
            # bc - index i has reached the end of the word, meaning all chars were matched successfully.
            if i == len(word):
                return True
            
            # mapping all failure conditions.
            if(r < 0 or c < 0 or
            r >= rows or c >= cols or
            word[i] != board[r][c] or
            (r, c) in path):
                return False

            # if the curr cell is valid and matches the word, mark it and store it inside the set
            path.add((r, c))

            # recursively trying all four neighbors
            res = (dfs(r + 1, c, i + 1) or 
            dfs(r - 1, c, i + 1) or 
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))

            # backtracking by removing the current cell from the path
            path.remove((r, c))

            return res

        # trying every cell in the grid as a potential starting point.
        for r in range(rows):
            for c in range(cols):
                # if dfs in this cell finds the full word, return True
                if dfs(r, c, 0):
                    return True

        return False

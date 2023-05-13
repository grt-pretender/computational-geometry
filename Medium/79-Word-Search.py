# Given an m x n grid of characters board and a string word, 
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()

# depth-first search function
        def dfs(r, c, i):

# reaching the end of the word
            if i == len(word):
                return True 

# out of range / wrong element
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False

            path.add((r,c))

            result = (dfs(r + 1, c, i + 1) or
    dfs(r - 1, c, i + 1) or
    dfs(r, c + 1, i + 1) or
    dfs(r, c - 1, i + 1))

            path.remove((r,c))
    
            return result

# using depth-first search for all cells in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(1, COLS):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        
        for i in range(1, ROWS):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        
        return grid[ROWS-1][COLS-1]
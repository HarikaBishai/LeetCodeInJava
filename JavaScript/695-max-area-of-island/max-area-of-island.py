class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r,c):
            area = 1
            dir = [(-1,0), (1,0),(0,1), (0,-1)]
            for i, j in dir:
                new_r = r + i
                new_c = c + j
                if new_r in range(ROWS) and new_c in range(COLS) and f'{new_r}-{new_c}' not in visited and grid[new_r][new_c] == 1:
                    visited.add(f'{new_r}-{new_c}')
                    area+= dfs(new_r, new_c)
            return area
        
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and  f'{i}-{j}' not in visited:
                    visited.add(f'{i}-{j}')
                    area = dfs(i, j)
                    maxArea = max(area, maxArea)
        return maxArea
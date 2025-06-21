class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        islands = 0
        visited = set()
        def dfs(r, c):
            visited.add((r,c))

            dir = [(-1, 0), (1,0), (0,-1), (0,1)]

            for i, j in dir:
                new_r = i + r
                new_c = j + c
                if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands+=1
                    dfs(i,j)

        return islands

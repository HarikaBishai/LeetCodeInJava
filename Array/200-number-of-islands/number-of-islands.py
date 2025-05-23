class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()


        def dfs(r, c):
            visited.add((r,c))
            
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]

            for i, j in dirs:
                new_r = r+i
                new_c = c+j
                if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c]=='1' and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
        

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and  (i,j) not in visited:
                    dfs(i,j)
                    islands+=1
        return islands 
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        dir = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(r, c, pr, pc):
            visited.add((r,c))
            for i,j in dir:
                new_r = i + r
                new_c = j + c
                if new_r not in range(m) or  new_c not in range(n):
                    continue 
                
                if grid[r][c] != grid[new_r][new_c]:
                    continue

                if (new_r, new_c) == (pr, pc):
                    continue
                
                if (new_r, new_c) in visited:
                    return True

                if dfs(new_r, new_c, r, c):
                        return True
            
           
            return False

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and dfs(i, j, -1,-1):
                    return True
        
        return False
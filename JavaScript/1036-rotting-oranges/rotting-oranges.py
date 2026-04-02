class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dir = [(-1,0),(1,0), (0,1), (0,-1)]

        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        time = 0
        while q:
            if fresh == 0:
                return time
            for _ in range(len(q)):
                r,c = q.popleft()

                for i, j in dir:
                    new_r = i + r
                    new_c = j + c
                    if 0<=new_r<=m-1 and 0<=new_c<=n-1 and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh-=1
                        q.append((new_r ,new_c))
            
            time+=1
        
        return time if fresh == 0 else -1


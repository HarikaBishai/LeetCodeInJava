class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }

        dirs = [(0,1), (0, -1), (1,0), (-1,0)] 

        dist = [[float('inf')]*n for _ in range(m)]

        dq = deque([(0,0)])

        dist[0][0] = 0

        while dq:
            r, c = dq.popleft()

            for i , j in dirs:
                new_r = r + i
                new_c = c + j
                if 0 <= new_r <= m-1 and 0 <= new_c <= n-1:
                    effort = 0 if directions[grid[r][c]] == (i,j) else 1
                    new_cost = dist[r][c] + effort
                    if dist[new_r][new_c] > new_cost:
                        dist[new_r][new_c] = new_cost
                        if effort == 1:
                            dq.append((new_r, new_c))
                        else:
                            dq.appendleft((new_r, new_c))
                        
        return dist[m-1][n-1]
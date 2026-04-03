class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dir = [(-1,0), (1,0),(0,-1), (0, 1) ]

        h = [(grid[0][0], 0,0)]

        best = { (0,0) : grid[0][0]}


        while h:
            t , r, c = heapq.heappop(h)

            if (r,c) in best and  best[(r,c)] < t:
                continue
            
            if r == m-1 and c == n-1:
                return t
            

            for i, j in dir:
                new_r = r+i
                new_c = c+j
                if 0<=new_r<=m-1 and 0<=new_c<=n-1:
                    new_best = max(t, grid[new_r][new_c])
                    if (new_r, new_c) not in best or best[(new_r, new_c)] > new_best:
                        best[(new_r, new_c)] = new_best
                        heapq.heappush(h, (new_best, new_r, new_c))
        return -1
        


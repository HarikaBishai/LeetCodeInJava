class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)

        n = len(heights[0])

        dist = [[float('inf')]*n for _ in range(m)]

        dist[0][0] = 0
        h = []
        heapq.heappush(h, (0,0,0))
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        while h:
            effort, r, c = heapq.heappop(h)
            if effort > dist[r][c]:
                continue
            
            if r == m-1 and c == n-1:
                return effort

            for i , j in dir:
                new_r = r + i
                new_c = c + j

                if 0 <= new_r<=m-1 and 0<=new_c<=n-1:
                    new_effort = max(effort, abs(heights[new_r][new_c] - heights[r][c]))
                    if new_effort < dist[new_r][new_c] :
                        dist[new_r][new_c] = new_effort
                        heapq.heappush(h, (new_effort, new_r, new_c))
        

            




class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
        ans = -1
        min_reachable = float('inf')


        for i in range(n):
            reachable = 0
            for j in range(n):
                if j!=i and dist[i][j] <= distanceThreshold:
                    reachable+=1
            if reachable <= min_reachable:
                min_reachable = reachable
                ans = i
        
        return ans
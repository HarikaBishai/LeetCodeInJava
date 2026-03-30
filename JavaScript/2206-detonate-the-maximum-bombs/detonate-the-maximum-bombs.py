class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {i: [] for i in range(n)}

        for i in range(n):
            x1,y1,r1 = bombs[i]
            for j in range(n):
                if i==j:
                    continue
                x2,y2,r2 = bombs[j]
                dx = x1-x2
                dy = y1-y2

                if dx*dx+ dy*dy <= r1*r1:
                    graph[i].append(j)
        
        def dfs(i, visited):
            visited.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei,visited)
        ans = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            ans = max(ans, len(visited))
        return ans

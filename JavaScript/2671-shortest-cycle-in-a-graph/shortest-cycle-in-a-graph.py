class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = float('inf')
        for i in range(n):
            dist = [-1]*n
            parent = [-1]*n
            q = deque([i])
            dist[i] = 0

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei == parent[node]:
                        continue
                    if dist[nei] != -1:
                        ans = min(ans, dist[node] + dist[nei]+1)
                    else:
                        dist[nei] = 1+dist[node]
                        parent[nei]= node
                        q.append(nei)
        return ans if ans!=float('inf') else -1
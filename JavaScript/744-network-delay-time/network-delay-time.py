class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i:[] for i in range(1, n+1)}

        for u,v,w in times:
            graph[u].append((v,w))

        h = [(0, k)]

        dist = [float('inf')]*n
        dist[k-1] = 0

        while h:
            t, node = heapq.heappop(h)

            if t > dist[node-1]:
                continue

            dist[node-1] = t

            for nei , nei_t in graph[node]:
                if t + nei_t < dist[nei-1]:
                    heapq.heappush(h,(t+nei_t, nei))

        ans = max(dist)

        return -1 if ans == float('inf') else ans
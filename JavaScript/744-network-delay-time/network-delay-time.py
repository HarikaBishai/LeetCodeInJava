class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i:[] for i in range(1, n+1)}

        for u,v,w in times:
            graph[u].append((v,w))

        h = [(0, k)]

        visited = set()

        time = 0
        while h:
            t, node = heapq.heappop(h)

            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                return t

            

            for nei , nei_t in graph[node]:
                if nei not in visited:
                    heapq.heappush(h,(t+nei_t, nei))

        return -1
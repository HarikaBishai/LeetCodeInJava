class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        visited = set()

        graph = {i:[] for i in range(1, n+1)}

        for u, v , cost in connections:
            graph[u].append((v,cost))
            graph[v].append((u,cost))

        h = [(0, 1)]
        min_cost = 0

        while h:
            cost, city = heapq.heappop(h)

            if city in visited:
                continue
            
            min_cost += cost
            visited.add(city)

            for nei, nei_cst in graph[city]:
                if nei not in visited:
                    heapq.heappush(h, (nei_cst, nei))

        
        return min_cost if len(visited) == n else -1
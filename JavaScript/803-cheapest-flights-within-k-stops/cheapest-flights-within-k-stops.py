class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}

        for u, v, cost in flights:
            graph[u].append((v,cost))


        h = [(0,0,src)]
        
        best = {(src, 0): 0}

        while h:
            cost, stop , city = heapq.heappop(h)

            if best[(city, stop)] < cost:
                continue
            
            if city == dst:
                return cost

            if stop == k+1:
                continue
            
            for nei, nei_cst in graph[city]:
                new_cost = nei_cst + cost
                if (nei, stop+1) not in best or best[(nei, stop+1)] > new_cost:
                    best[(nei, stop+1)] = new_cost
                    heapq.heappush(h, (new_cost, stop+1, nei))

        return -1
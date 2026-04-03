class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        if len(points) == 1:
            return 0
        
        n = len(points)
        visited = set()
        min_cost = 0

        h = [(0, 0)]

        while h:
            cost , pt = heapq.heappop(h)

            if pt in visited:
                continue
                
            visited.add(pt)
            min_cost+= cost

            for i in range(n):
                if i!=pt and i not in visited:
                    x1,y1 = points[pt]
                    x2,y2 = points[i]

                    new_cost = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(h, (new_cost, i))
        return min_cost
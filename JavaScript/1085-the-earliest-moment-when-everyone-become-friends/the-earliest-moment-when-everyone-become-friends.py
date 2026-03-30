class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        parents = [i for i in range(n)]
        rank = [1]*n
        components = n

        def find(x):
            if parents[x]!=x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x,y):
            nonlocal components
            parentX = find(x)
            parentY = find(y)
            if parentX == parentY:
                return 
            
            rankParentX = rank[parentX]
            rankParentY = rank[parentY]
            if rankParentX > rankParentY:
                parents[parentY] = parentX
                rank[parentX]+=1
            elif rankParentX < rankParentY:
                parents[parentX] = parentY
                rank[parentY]+=1
            else:
                parents[parentY] = parentX
                rank[parentX]+=1
            components-=1
            return 

        for time, x, y in logs:
            union(x,y)
            if components == 1:
                return time
        return -1



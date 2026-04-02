class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = {}
        rank = defaultdict(int)

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        

        def union(u,v):
            parentu = find(u)
            parentv = find(v)
            

            if parentu == parentv:
                return True
            ranku = rank[parentu]
            rankv = rank[parentv]

            if ranku < rankv:
                parent[parentu] = parentv
            elif rankv < ranku:
                parent[parentv] = parentu
            else:
                parent[parentu] = parentv
                rank[parentu]+=1

            return False

        lastEdge = [-1,-1]
        for u,v in edges:
            res = union(u,v)
            if res:
                lastEdge = [u,v]
        return lastEdge



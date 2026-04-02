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
            print(parentu, parentv)
            ranku = rank[parentu]
            rankv = rank[parentv]

            if parentu == parentv:
                return True
            
            if ranku < rankv:
                parent[parentu] = parentv
                rank[parentv]+=1
            else:
                parent[parentv] = parentu
                rank[parentu]+=1

            return False

        lastEdge = [-1,-1]
        for u,v in edges:
            res = union(u,v)
            print(res, u, v)
            if res:
                lastEdge = [u,v]
        return lastEdge



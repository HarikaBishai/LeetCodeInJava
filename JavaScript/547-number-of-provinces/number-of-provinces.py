class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if j!=i and isConnected[i][j] == 1:
                    graph[i].append(j)
        
        visited = set()


        n = len(isConnected)
        count = 0

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
            
        return count
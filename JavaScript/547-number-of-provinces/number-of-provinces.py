class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        visited = set()


        n = len(isConnected)
        count = 0

        def dfs(node):
            visited.add(node)

            for nei in range(n):
                if nei not in visited and isConnected[node][nei] == 1:
                    dfs(nei)
            
        for city in range(n):
            if city not in visited:
                dfs(city)
                count+=1
            
        return count
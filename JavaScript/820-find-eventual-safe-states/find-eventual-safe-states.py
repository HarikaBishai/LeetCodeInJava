class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in safe:
                return safe[node]
            
            path.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    path.remove(node)
                    safe[node] = False
                    return False
            path.remove(node)
            safe[node] = True
            return True
        
        out = []

        for i in range(len(graph)):
            if dfs(i):
                out.append(i)
        return out
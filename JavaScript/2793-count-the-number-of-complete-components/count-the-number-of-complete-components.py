class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, component)

        count = 0
        for i in range(n):
            if i not in visited:
                component= []
                dfs(i, component)
                size = len(component)
                if all(len(graph[node])  == size - 1 for node in component):
                    count+=1
        return count



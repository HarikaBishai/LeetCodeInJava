class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque()
        visited = set()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                

        while q:
            node = q.popleft()
            visited.add(node)
            if len(visited) == numCourses:
                return True
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return False
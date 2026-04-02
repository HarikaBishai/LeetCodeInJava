class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque()
        out = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            out.append(curr)
            if len(out) == numCourses:
                return out
            
            for nei in graph[curr]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return []
            
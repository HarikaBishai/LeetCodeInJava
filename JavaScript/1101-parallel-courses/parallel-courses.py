class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(1,n+1)}
        indegree = {i:0 for i in range(1,n+1)}

        for u, v in relations:
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque()

        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)

        taken = 0
        semesters = 0

        while q:
            semesters+=1
            for _ in range(len(q)):
                
                curr = q.popleft()
                taken+=1
                
                for nei in graph[curr]:
                    indegree[nei]-=1
                    if indegree[nei] == 0:
                        q.append(nei)
        
        return semesters if taken == n else -1 
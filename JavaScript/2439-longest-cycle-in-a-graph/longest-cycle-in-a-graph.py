class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        ans = -1
        for i in range(n):
            if i in visited:
                continue

            curr = i
            dist = {}
            steps = 0
            while curr!=-1 and curr not in visited:
                visited.add(curr)
                dist[curr] = steps
                steps+=1
                curr = edges[curr]

            if curr!=-1 and curr in dist:
                ans = max(ans, steps-dist[curr])
        return ans
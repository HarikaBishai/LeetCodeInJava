class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = '0000'
        if start in deadends or target in deadends:
            return -1

        q = deque([start])
        visited = set([start])

        steps = 0
        while q:
            
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                
                dir = [-1, 1]
                for i in range(4):
                    for j in dir:
                        new = curr[:i] + str((int(curr[i]) + j) % 10) + curr[i+1:]

                        if new not in visited and new not in deadends:
                            visited.add(new)
                            q.append(new)
            steps+=1
        return -1
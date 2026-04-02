class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        

        m = len(rooms)
        n = len(rooms[0])
        INF = 2147483647
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))

        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        level = 0 
        while q:
            level+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for i, j in dir:
                    new_r = r+i
                    new_c = c+j
                    if new_r in range(m) and new_c in range(n) and rooms[new_r][new_c] == INF:
                        rooms[new_r][new_c] = level
                        q.append((new_r, new_c))
        
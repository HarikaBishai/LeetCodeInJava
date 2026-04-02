class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = set()
        dir = [(-1,0), (1,0), (0,-1),(0,1)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        level = 0
        while q:
            level+=1
            for _ in range(len(q)):
                r,c = q.popleft()

                for i, j in dir:
                    new_r = r + i
                    new_c = c + j
                    if 0<= new_r <= m-1 and 0<= new_c <= n-1 and (new_r, new_c) not in visited:
                        mat[new_r][new_c] = level
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))

        return mat
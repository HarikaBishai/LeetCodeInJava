class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        m = len(image)
        n = len(image[0])

        q = deque([(sr, sc)])
        visited = set([(sr, sc)])

        initial = image[sr][sc]
        while q:
            print(q)
            r, c = q.popleft()

            image[r][c] = color
            
            dir = [(-1,0), (1,0), (0,1), (0, -1)]

            for i, j in dir:
                new_r = r + i 
                new_c = c + j
                if new_r in range(m) and new_c in range(n) and (new_r, new_c) not in visited and image[new_r][new_c]==initial:
                    visited.add((new_r, new_c))
                    q.append((new_r, new_c))
        return image
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        org_color = image[sr][sc]

        if color == org_color:
            return image
        def dfs(r, c):
            # visited.add(r,c)
            image[r][c] = color
            dirs = [(-1,0), (1,0), (0,1), (0,-1)]

            for i, j in dirs:
                new_r = i + r
                new_c = j + c
                if 0<=new_r<ROWS and 0<=new_c<COLS and image[new_r][new_c] == org_color:
                    dfs(new_r , new_c)
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if image[i][j] == org_color:
        #             dfs(i , j)
        dfs(sr, sc)
        return image

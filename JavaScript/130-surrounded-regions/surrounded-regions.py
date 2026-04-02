class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        visited = set()
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        def dfs(r,c):
            board[r][c] = '#'

            for i , j in dir:
                new_r = r + i
                new_c = c + j
                if new_r in range(m) and new_c in range(n) and board[new_r][new_c] == 'O':
                    dfs(new_r, new_c)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[m-1][i] == 'O':
                dfs(m-1,i)

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
            
        
             

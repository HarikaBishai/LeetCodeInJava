class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                if val!='.':
                    if val in rows[i] or val in cols[j] or val in grid[(i//3, j//3)]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    grid[(i//3, j//3)].add(val)
        return True
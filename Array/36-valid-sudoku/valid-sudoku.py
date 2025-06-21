from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        n = len(board)
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val!='.':
                    if val in rows[i] or val in cols[j] or val in grids[(i//3, j//3)]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    grids[(i//3, j//3)].add(val)
        return True

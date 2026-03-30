class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir= {
            'R': [0, 1],
            'L': [0, -1],
            'U': [-1, 0],
            'D': [1, 0]
        }

        start = [0,0]
        curr = start
        for move in moves:
            i,j = dir[move]
            curr = [i+curr[0], j + curr[1]]
        
        return start == curr
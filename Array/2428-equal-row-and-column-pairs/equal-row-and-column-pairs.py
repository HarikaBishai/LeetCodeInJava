class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = {}
    
        count = 0
        n = len(grid)
        for i in range(n):
            t = tuple(grid[i][:])
            if t in row_count:
                row_count[t]+=1
            else:
                row_count[t]=1


        for i in range(n):
            t = ()
            for j in range(n):
                t += (grid[j][i], )
            print(t)
            if t in row_count:
                count+=row_count[t]
            
        return count



        

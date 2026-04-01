class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []

        def dfs(i, curr, total):
            if len(curr) == k:
                if total == n:
                    res.append(curr[:])
                return 
            if total > n:
                return

            for j in range(i, 10):
                curr.append(j)
                dfs(j+1, curr, total+j)
                curr.pop()
        
        dfs(1,[], 0)

        return res
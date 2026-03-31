class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(i, curr, total + candidates[i])
                curr.pop()
            return
        
        dfs(0, [], 0)
        return res
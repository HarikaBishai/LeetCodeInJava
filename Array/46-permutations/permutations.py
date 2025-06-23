class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = set()
        stk = []
        n = len(nums)
        out = []

        def dfs():
            if len(stk) == n:
                out.append(stk[:])
                return

            for num in nums:
                if num not in path:
                    path.add(num)
                    stk.append(num)
                    dfs()
                    path.remove(num)
                    stk.pop()
        dfs()
        return out
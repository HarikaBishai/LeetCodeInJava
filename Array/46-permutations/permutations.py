class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stk = []
        path = set()
        out = []

        def dfs():
            if len(stk) == len(nums):
                out.append(stk.copy())

            for num in nums:
                if num not in path:
                    path.add(num)
                    stk.append(num)
                    dfs()
                    path.remove(num)
                    stk.pop()
        dfs()
        return out
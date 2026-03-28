class Solution:
    def pathSum(self, nums: List[int]) -> int:
        mp = {num//10:num%10 for num in nums}

        total = 0

        def dfs(node_key, currSum):
            nonlocal total

            if node_key not in mp:
                return
            
            currSum += mp[node_key]

            d,p = divmod(node_key, 10)
            left = (d + 1) * 10 + (2 * p-1)
            right = (d + 1) * 10 + (2 * p)

            if left not in mp and right not in mp:
                total+=currSum
                return
            dfs(left, currSum)
            dfs(right, currSum)
        dfs(11, 0)
        return  total
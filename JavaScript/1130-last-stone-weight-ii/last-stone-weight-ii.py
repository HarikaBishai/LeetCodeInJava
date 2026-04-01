class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneTotal = sum(stones)
        total = stoneTotal // 2

        dp = [False]*(total+1)
        dp[0] = True

        for s in stones:
            for t in range(total, s-1, -1):
                dp[t] = dp[t] or dp[t-s]
        
        for i in range(total, -1, -1):
            if dp[i]:
                return stoneTotal - 2*i
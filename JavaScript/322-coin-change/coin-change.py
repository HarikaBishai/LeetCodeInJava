class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for t in range(coin, amount+1):
                dp[t] = min(dp[t], 1+dp[t-coin])
        
        return dp[amount] if dp[amount]!=float('inf') else -1

        # dp = [[float('inf')]*(amount+1) for _ in range(n+1)]

        # for i in range(n+1):
        #     dp[i][0] = 0

        # for i in range(1, n+1):
        #     coin = coins[i-1]

        #     for t in range(1, amount+1):
        #         dp[i][t] = dp[i-1][t]

        #         if t>=coin:
        #             dp[i][t] = min(dp[i][t], 1+dp[i][t-coin])

        return dp[n][amount] if dp[n][amount]!=float('inf') else -1

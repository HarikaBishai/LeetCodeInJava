class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        i = 1
        while i * i <= n:
            squares.append(i * i )
            i+=1
        
        dp = [float('inf')]*(n+1)

        dp[0] = 0

        for sq in squares:
            for i in range(sq, n+1):
                dp[i] = min(dp[i], 1+dp[i-sq])
        return dp[n]
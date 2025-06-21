class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(1, len(prices)):
            currProfit = max(prices[i]-prices[i-1], 0)
            profit+=currProfit
        
        return profit
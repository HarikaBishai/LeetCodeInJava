class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        max_right = prices[-1]
       
        for i in range(len(prices)-2, -1, -1):
            max_right = max(prices[i], max_right)
            max_profit = max(max_profit, max_right-prices[i])
        return max_profit
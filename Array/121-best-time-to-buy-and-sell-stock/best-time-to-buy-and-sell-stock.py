class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxPrice = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            maxProfit = max(maxProfit, maxPrice - prices[i])
        return maxProfit
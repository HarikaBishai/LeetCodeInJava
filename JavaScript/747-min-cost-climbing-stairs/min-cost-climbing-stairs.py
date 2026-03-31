class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost)


        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            temp =  cost[i]+min(prev2, prev1)
            prev2 = prev1
            prev1 = temp

        return min(prev2, prev1)
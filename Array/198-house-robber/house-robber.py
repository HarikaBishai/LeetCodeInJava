class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = max(rob2, rob1+num)
            rob1 = rob2
            rob2 = temp
        
        return max(rob1, rob2)
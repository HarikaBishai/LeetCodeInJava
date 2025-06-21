class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = float('-inf')

        maxSum = float('-inf')

        for num in nums:
            currSum = max(currSum+num, num)
            maxSum = max(maxSum, currSum)
        return maxSum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSum = {}

        for i in range(len(nums)):
            num = nums[i]
            if target-num in seenSum:
                return [seenSum[target-num], i]
            seenSum[num] = i
        return [-1,-1]
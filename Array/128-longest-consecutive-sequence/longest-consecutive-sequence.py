class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxLen = 0
        for num in nums_set:
            if num-1 not in nums_set:
                count = 1
                while num+count in nums_set:
                    count+=1
                
                maxLen = max(maxLen, count)

        return maxLen

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        max_cons = 0
        count = 0
        
        for r in range(len(nums)):
            if nums[r] == 1:
                count+=1
            while l<len(nums) and (r-l+1)-count > 1:
                if nums[l] == 1:
                    count-=1
                l+=1
            max_cons = max(max_cons, count)
        
        return max_cons if max_cons <len(nums) else max_cons-1
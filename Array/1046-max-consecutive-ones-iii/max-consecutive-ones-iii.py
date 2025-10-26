class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_cons = 0
        l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count +=1
            while l<len(nums) and (r-l+1)-count > k:
                if nums[l] == 1:
                    count -=1
                l+=1
            max_cons = max(max_cons, r-l+1)
        return max_cons

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        out = 0
        l = 0
        for r in range(len(nums)):
            prod*= nums[r]
            while l<=r and prod >= k:
                prod //=nums[l]
                l+=1
            out+=r-l+1
        
        return out
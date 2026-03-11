class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)
        left = 1
        for i in range(1,len(nums)):
            out[i] = left * nums[i-1]
            left = left * nums[i-1]


        right = 1
        for i in range(len(nums)-2, -1, -1):
            right = right * nums[i+1]
            out[i] *= right
        
        return out

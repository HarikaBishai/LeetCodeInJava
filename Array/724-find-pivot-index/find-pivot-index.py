class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum = [0]*len(nums)
        right_sum = [0]*len(nums)


        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]
        
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
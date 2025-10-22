class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero_idx = 0

        for i in range(0, len(nums)):
            if nums[i]!=0:
                nums[i], nums[nonzero_idx] = nums[nonzero_idx], nums[i]
                nonzero_idx+=1
            
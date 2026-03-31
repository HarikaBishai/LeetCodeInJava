class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max = nums[0]
        curr_min = nums[0]

        maxProduct = nums[0]

        for i in range(1, len(nums)):
            temp = max(curr_max*nums[i], curr_min*nums[i], nums[i])
            curr_min = min(curr_max*nums[i], curr_min*nums[i], nums[i])
            curr_max = temp
            maxProduct = max(curr_max, curr_min, maxProduct)

        return maxProduct
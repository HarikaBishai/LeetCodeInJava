class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstpos = -1
        lastpos = -1

        n = len(nums)
        l = 0
        r = n-1

        while l<=r:
            m = (l+r)//2
            if nums[m] >= target:
                firstpos = m
                r = m-1
            else:
                l = m+1

        
        if firstpos == -1 or nums[firstpos]!= target:
            return [-1,-1]
        
        l = 0
        r = n-1

        while l<=r:
            m = (l+r)//2
            if nums[m] <= target:
                lastpos = m
                l = m+1
            else:
                r = m-1
        
        return [firstpos, lastpos]
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        out = set()
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    out.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    r-=1
        return list(out)

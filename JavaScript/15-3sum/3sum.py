class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = set()
        n = len(nums)

        nums.sort()

        for i in range(0, n-2):
            
            l = i+1
            r = n-1

            while l<r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    out.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif curr < 0:
                    l+=1
                else:
                    r-=1
        
        return list(out)
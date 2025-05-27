class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()

        n = len(nums)

        for i in range(n-2):
            l = i+1
            r = n-1

            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.add((nums[i] , nums[l] , nums[r]))
                    l+=1
                    r-=1
                elif sum > 0:
                    r-=1
                else:
                    l+=1
        return list(result)
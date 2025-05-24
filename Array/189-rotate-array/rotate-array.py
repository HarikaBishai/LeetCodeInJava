class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 4 3 2 1 7 6 5

        # 5 6 7 1 2 3 4 

        
        def reverse(start, end):

            l = start
            r = end
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        n = len(nums)
        k = k%n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        
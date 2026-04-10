class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        stk = []

        for i in range(len(nums)):
            while stk and stk[-1][1] < nums[i]:
                stk.pop()
            stk.append([i, nums[i]])

            if stk and stk[0][0] < i-k+1:
                stk.pop(0)

            if i >= k-1:
                out.append(stk[0][1])
        return out
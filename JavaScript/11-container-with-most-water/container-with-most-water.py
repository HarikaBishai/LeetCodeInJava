class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1

        water = 0

        while l<r:
            if height[l] < height[r]:
                water = max(water,(r-l)* height[l])
                l+=1
            else:
                water = max(water,(r-l)* height[r])
                r-=1
        return water

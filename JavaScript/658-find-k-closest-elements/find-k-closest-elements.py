class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        r = n-1

        l = 0
        while l<r:
            m = (l+r)//2

            if m+k < n and  x-arr[m] > arr[m+k]-x:
                l= m+1
            else:
                r=m
        return arr[l:l+k]
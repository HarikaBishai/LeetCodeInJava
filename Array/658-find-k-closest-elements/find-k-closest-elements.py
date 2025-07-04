class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n-k

        while l<r:
            m = (l+r)//2

            if x-arr[m] > arr[m+k] - x:
                l=m+1
            else:
                r=m
        return arr[l:l+k]
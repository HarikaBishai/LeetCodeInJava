class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxVal = max([x for x in candies])
        out = [True if x+extraCandies >= maxVal else False for x in candies  ]
        return out
       

        
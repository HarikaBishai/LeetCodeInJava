from bisect import bisect_left, bisect_right
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        starts = [x[0] for x in intervals]
        ends = [x[1] for x in intervals]

        new_start, new_end = newInterval

        left = bisect_left(ends, new_start)
        right = bisect_right(starts, new_end)
        
        if left < right:
            new_start = min(new_start, intervals[left][0])
            new_end = max(new_end, intervals[right-1][1])

        merged = intervals[:left] + [[new_start, new_end] ]+ intervals[right:]
        return merged

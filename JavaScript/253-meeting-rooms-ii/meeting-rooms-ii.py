import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        h = []
        out = 0

        for start, end in intervals:

            if h and h[0] <= start:
                heapq.heapreplace(h,end)
            else:
                out+=1
                heapq.heappush(h,end)
        return out

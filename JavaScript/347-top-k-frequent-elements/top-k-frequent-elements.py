import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        counter = Counter(nums)

        for key, val in counter.items():
            heapq.heappush(h, (val, key))
            if len(h) > k:
                heapq.heappop(h)
        
        out = []

        while h:
            out.append(heapq.heappop(h)[1])
        
        return out
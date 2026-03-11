import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h = []

        for key,val in counter.items():
            heapq.heappush(h, (val, key) )
            if len(h) > k:
                heapq.heappop(h)
            
        
        out = []
        while h:
            out.append(heapq.heappop(h)[1])
        return out
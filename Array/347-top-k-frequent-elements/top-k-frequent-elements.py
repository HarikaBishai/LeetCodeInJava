from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []

        for num, count in counter.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        

        out = []

        while heap:
            count, num = heapq.heappop(heap)
            out.append(num)
        return out
            

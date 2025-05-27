import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []

        counter = Counter(tasks)

        for key, count in counter.items():
            heapq.heappush(maxHeap, -count)

        q = deque()

        time = 0

        while maxHeap or q:
            time+=1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap)+1
                if cnt:
                    q.append((cnt, time+n))
            
            if q and  time == q[0][1]:
                cnt = q.popleft()[0]
                heapq.heappush(maxHeap, cnt)
        return time
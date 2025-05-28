from sortedcontainers import SortedList
import heapq
from typing import List
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        count = [0] * k

        busy, free = [], SortedList(list(range(k)))


        for i in range(len(arrival)):
            start = arrival[i]
            while busy and busy[0][0] <= start:
                time, busy_id = heapq.heappop(busy)
                free.add(busy_id)
            if free:
                idx = free.bisect_left(i%k)
                server_id = free[idx] if idx < len(free) else free[0]
                count[server_id]+=1
                free.remove(server_id)
                heapq.heappush(busy, (start+load[i], server_id))
        max_count = max(count)

        return [idx for idx, cnt in enumerate(count) if cnt == max_count ]

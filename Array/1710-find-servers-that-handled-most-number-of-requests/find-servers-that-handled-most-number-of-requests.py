from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy, free = [], SortedList(list(range(k)))
        count =[0] * k

        for i in range(len(arrival)):
            start = arrival[i]
            while busy and busy[0][0]<=start:
                time, server_id = heapq.heappop(busy)
                free.add(server_id)
            
            if free:
                idx = free.bisect_left(i%k)
                server_id = free[idx] if idx < len(free) else free[0]
                count[server_id]+=1
                free.remove(server_id)
                heapq.heappush(busy, (start+load[i],server_id ))

        max_count = max(count)

        return [idx for idx, val in enumerate(count) if val == max_count]

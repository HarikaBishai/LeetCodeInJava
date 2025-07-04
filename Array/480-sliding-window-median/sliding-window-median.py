import heapq
from collections import defaultdict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap = []
        minHeap = []
        smallCount = 0
        largeCount = 0
        delayed = defaultdict(int)


        def add(num):
            nonlocal smallCount
            nonlocal largeCount
            if not maxHeap or num <= -maxHeap[0]:
                smallCount+=1
                heapq.heappush(maxHeap, -num)
            else:
                largeCount+=1
                heapq.heappush(minHeap, num)
            balance()
        

        def remove(num):
            nonlocal smallCount
            nonlocal largeCount
            delayed[num]+=1

            if num<=-maxHeap[0]:
                smallCount-=1
                if maxHeap[0] == -num:
                    shrink(maxHeap)
            else:
                largeCount-=1
                if minHeap[0] == num:
                    shrink(minHeap)
            balance()

        
        def balance():
            nonlocal smallCount
            nonlocal largeCount
            while smallCount > largeCount+1:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                smallCount-=1
                largeCount+=1
                shrink(maxHeap)
            while largeCount > smallCount:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                smallCount+=1
                largeCount-=1
                shrink(minHeap)
            
            
        
        def shrink(heap):
            while heap and delayed.get((val:= -heap[0] if heap == maxHeap else heap[0]), 0):
                delayed[val]-=1
                heapq.heappop(heap)
                if delayed[val] == 0:
                    del delayed[val]
            
        
        def getMedian():
            if k % 2:
                return float(-maxHeap[0])
            else:
                return (-maxHeap[0] + minHeap[0]) / 2
            
        result = []
        for i in range(len(nums)):
            add(nums[i])
            if i >=k-1:
                result.append(getMedian())
                remove(nums[i-k+1])
        return result


        

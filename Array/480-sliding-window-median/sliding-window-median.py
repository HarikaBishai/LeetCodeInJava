
import heapq
from collections import defaultdict
from typing import List

class MedianFinder:
    def __init__(self, k: int):
        self.k = k  # size of the sliding window
        self.small_max_heap = []  # max heap to store the smaller half of numbers
        self.large_min_heap = []  # min heap to store the larger half of numbers
        self.delayed = defaultdict(int)  # count of delayed elements for lazy deletion
        self.small_size = 0  # size of small_max_heap (not necessarily len(small_max_heap))
        self.large_size = 0  # size of large_min_heap (not necessarily len(large_min_heap))

    def add_num(self, num: int):
        # Add a number to one of the heaps
        if not self.small_max_heap or num <= -self.small_max_heap[0]:
            heapq.heappush(self.small_max_heap, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large_min_heap, num)
            self.large_size += 1
        self.rebalance()

    def find_median(self) -> float:
        # Find the median of the current numbers
        return -self.small_max_heap[0] if self.k % 2 == 1 else (-self.small_max_heap[0] + self.large_min_heap[0]) / 2

    def remove_num(self, num: int):
        # Lazily remove a number (the number will be removed later during pruning)
        self.delayed[num] += 1
        if num <= -self.small_max_heap[0]:
            self.small_size -= 1
            if num == -self.small_max_heap[0]:
                self.prune(self.small_max_heap)
        else:
            self.large_size -= 1
            if num == self.large_min_heap[0]:
                self.prune(self.large_min_heap)
        self.rebalance()

    def prune(self, heap: List[int]):
        while heap:
            if heap is self.small_max_heap:
                num = -heap[0]
            else:
                num = heap[0]
            if self.delayed[num] > 0:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
                heapq.heappop(heap)
            else:
                break


    def rebalance(self):
        # Balance the two heaps to maintain the invariant small_max_heap.size() > large_min_heap.size()
        while self.small_size > self.large_size + 1:
            heapq.heappush(self.large_min_heap, -heapq.heappop(self.small_max_heap))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small_max_heap)
        while self.small_size < self.large_size:
            heapq.heappush(self.small_max_heap, -heapq.heappop(self.large_min_heap))
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large_min_heap)

class Solution:
    def medianSlidingWindow(self, nums, k):
        finder = MedianFinder(k)
        for x in nums[:k]:
            finder.add_num(x)
        medians = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add_num(nums[i])
            finder.remove_num(nums[i - k])
            medians.append(finder.find_median())
        return medians

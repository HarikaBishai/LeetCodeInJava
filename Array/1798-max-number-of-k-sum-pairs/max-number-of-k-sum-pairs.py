class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        found_sum = defaultdict(int)
        count = 0
        for num in nums:
            if (k-num) in found_sum:
                count+=1
                found_sum[k-num]-=1
                if found_sum[k-num] == 0:
                    del found_sum[k-num]
            else:
                found_sum[num] += 1
        return count
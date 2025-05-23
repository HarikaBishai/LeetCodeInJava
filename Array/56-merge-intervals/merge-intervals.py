class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stk = []

        intervals.sort()

        for start, end in intervals:
            if stk and stk[-1][1] >= start:
                last = stk.pop()
                stk.append([last[0], max(last[1], end)])
            else:
                stk.append([start, end])
        
        return stk
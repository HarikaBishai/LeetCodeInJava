class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stk = []

        for start, end in intervals:
            if stk and stk[-1][1] >= start:
                stk[-1][1] = max(end,  stk[-1][1]) 
            else:
                stk.append([start, end])
        return stk
                
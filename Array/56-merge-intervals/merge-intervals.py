class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stk = []
        intervals.sort()

        for st, end in intervals:
            if stk and stk[-1][1] >= st:
                top = stk.pop()
                stk.append([top[0], max(end, top[1])])
            else:
                stk.append([st, end])
        return stk
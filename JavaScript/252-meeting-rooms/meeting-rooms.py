class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        stk = []

        for start, end in intervals:
               
            if stk:
                top = stk[-1]
                if start < top[1]:
                    return False
            stk.append([start, end])
        return True
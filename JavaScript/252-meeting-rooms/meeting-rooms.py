class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        stk = []

        for start, end in intervals:
               
            if stk and start < stk[-1][1]:
                    return False
            stk.append([start, end])
        return True
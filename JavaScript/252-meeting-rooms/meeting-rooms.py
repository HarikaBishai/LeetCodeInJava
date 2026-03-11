class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        stk = []

        for start, end in intervals:
            if stk and stk[-1][1] > start:
                return False
            stk.append([start, end])
        
        return True
from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True
        s_left = 0
        t_left = 0
        while s_left < len(s) and t_left < len(t):
            if s[s_left] == t[t_left]:
                s_left+=1
            t_left+=1
        return s_left == len(s)
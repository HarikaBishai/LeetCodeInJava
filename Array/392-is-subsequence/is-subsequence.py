from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True
        count = 0
        i = 0
        while i < len(t):
            while i < len(t) and count < len(s) and s[count] == t[i]:
                i+=1
                count+=1
            if count == len(s):
                return True
            i+=1
        return False
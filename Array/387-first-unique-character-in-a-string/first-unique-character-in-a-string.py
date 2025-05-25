from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for i in range(len(s)):
            c = s[i]

            if counter[c] == 1:
                return i
        return -1
        
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
        for i in range(len(s)):
            c = s[i]

            if counter[c] == 1:
                return i
        return -1
        
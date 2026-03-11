class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        l = 0
        minLen = float('inf')

        counter_s = defaultdict(int)
        target_seen = set()
        target_l = 0
        target_r = 0
        for r in range(len(s)):
            counter_s[s[r]] +=1
            if s[r] in counter_t:
                if counter_s[s[r]] == counter_t[s[r]]:
                    target_seen.add(s[r])
                while len(target_seen) == len(counter_t):
                    if( r-l+1 < minLen):
                        minLen = r-l+1
                        target_l = l
                        target_r = r
                    counter_s[s[l]] -=1
                    if s[l] in counter_t and counter_s[s[l]] <  counter_t[s[l]]:
                        target_seen.remove(s[l])
                    l+=1
        
        return "" if minLen == float('inf') else  s[target_l: target_r+1]
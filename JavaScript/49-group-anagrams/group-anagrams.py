from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_groups = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            sorted_groups[sorted_s].append(s)
        
        return list(sorted_groups.values())
            

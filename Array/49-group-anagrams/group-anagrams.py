from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            char_list = list(s)
            char_list.sort()
            groups["".join(char_list)].append(s)

            # groups["".join(sorted(s))].append(s)
        
        return list(groups.values())


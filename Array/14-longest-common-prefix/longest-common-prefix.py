class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float('inf')

        for s in strs:
            if len(s) < minLen:
                minLen = len(s)

        
        longestMatch = ""

        for i in range(minLen):
            currStr = strs[0][:i+1]
            j = 1
            while j < len(strs):
                if currStr != strs[j][:i+1]:
                    break
                j+=1
            if j == len(strs):
                longestMatch = currStr
            else:
                break
            
        return longestMatch


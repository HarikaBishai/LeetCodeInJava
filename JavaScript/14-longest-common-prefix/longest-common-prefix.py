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

            while j < len(strs) and strs[j].startswith(currStr):
                j+=1
            
            print(j)
            if j == len(strs):
                longestMatch = currStr
            else:
                break
            
        return longestMatch


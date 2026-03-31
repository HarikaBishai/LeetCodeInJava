class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        wordDict = set(wordDict)

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in wordDict:
                    if dfs(i+len(word)):
                        dp[i]= True
                        return True
               
                    
            dp[i] = False
            return False
        return dfs(0)
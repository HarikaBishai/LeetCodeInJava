class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return [""]
            
            res = []

            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in wordDict:
                    suffix = dfs(j)
                    for sentence in suffix:
                        if sentence == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sentence)
            
            memo[i] = res
            return res
        return dfs(0)
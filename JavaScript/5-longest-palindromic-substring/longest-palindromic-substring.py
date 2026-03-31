class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) <= 1:
        #     return s
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]

        # for i in range(n):
        #     dp[i][i] = True
        
        # maxLength = 1
        # start = 0

        # for length in range(2, n+1):
        #     for i in range(n-length+1):
        #         j = i+length-1
        #         if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
        #             dp[i][j]=True
        #             if length > maxLength:
        #                 maxLength = length
        #                 start = i
        
        # return s[start: start+maxLength]
        maxLen = 0
        start = 0
        n = len(s)
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    start = l
                l -=1
                r+=1
            
            l = i
            r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    start = l
                l -=1
                r+=1
        return s[start: start+maxLen]

        
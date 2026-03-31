class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <=1:
            return 1
        n = len(s)
        count = 0
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
                count+=1
            l = i
            r = i+1
            while  l >= 0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
                count+=1
        return count

        # for i in range(n):
        #     dp[i][i] = True
        
        # count = 0

        # for length in range(1, n+1):
        #     for i in range(n-length+1):
        #         j = i + length - 1
        #         if s[i] == s[j] and (length <= 2 or  dp[i+1][j-1]):
        #             dp[i][j] = True
        #             count+=1
        # return count
                    

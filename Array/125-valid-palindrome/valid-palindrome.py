class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        n = len(s)
        l = 0
        r = n-1

        while l<=r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
            elif s[l].isalnum():
                r-=1
            elif s[r].isalnum():
                l+=1
            else:
                r-=1
                l+=1
        return True


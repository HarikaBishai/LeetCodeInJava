class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count  = 0

        vowels = set({'a', 'e', 'i', 'o', 'u'})
        max_vowels = 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            while l < len(s) and r-l+1 > k:
                if s[l] in vowels:
                    count-=1
                l+=1
            max_vowels = max(count, max_vowels)
        return max_vowels
            

        
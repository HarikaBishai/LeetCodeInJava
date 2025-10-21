class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        l1, l2 = 0, 0
        n1, n2 = len(word1), len(word2)

        for idx, c in enumerate(word1):
            merged += c
            if idx < len(word2):
                merged += word2[idx]
        
        for i in range(idx+1, len(word2)):
            merged += word2[i]

        return merged


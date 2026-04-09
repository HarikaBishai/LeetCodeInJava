class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       
        l1 = len(word1)
        l2 = len(word2)

        merged = ""

        for i in range(min(l1, l2)):
            merged += word1[i]
            merged += word2[i]
            i+=1
        
        if i < l1:
            merged += word1[i:]
        
        if i < l2:
            merged += word2[i:]

        return merged
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        l1, l2 = 0, 0
        n1, n2 = len(word1), len(word2)

        i = 0
        while l1 < n1 or l2 < n2:
            if l1 < n1 and l2 < n2:
                merged += word1[l1]
                merged += word2[l2]
                l1+=1
                l2+=1
            elif l1 < n1:
                merged += word1[l1]
                l1+=1
            else:
                merged+= word2[l2]
                l2+=1
        return merged


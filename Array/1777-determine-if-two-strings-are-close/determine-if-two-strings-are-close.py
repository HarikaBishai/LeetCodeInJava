class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)

        values_count1 = Counter(count1.values())
        values_count2 = Counter(count2.values())


        return set(count1.values()) == set(count2.values()) and set(count1.keys()) == set(count2.keys()) and values_count1 == values_count2
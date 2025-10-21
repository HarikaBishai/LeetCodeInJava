class Solution:
    def reverseWords(self, s: str) -> str:
        words = [x for x in s.split(" ") if x.strip()]
        words.reverse()
        return " ".join(words)
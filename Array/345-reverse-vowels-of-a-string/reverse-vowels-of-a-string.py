class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        arr = list(s)

        l = 0
        r = len(s)-1
        while l<r:
            if arr[r] in vowels and arr[l] in vowels:
                arr[r], arr[l] = arr[l], arr[r]
                r-=1
                l+=1
            elif arr[r] in vowels:
                l+=1
            elif arr[l] in vowels:
                r-=1
            else:
                l+=1
                r-=1
        return "".join(arr)
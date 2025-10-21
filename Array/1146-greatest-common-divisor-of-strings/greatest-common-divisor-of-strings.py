class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def is_divisor(i):
            if len(str1)%i or len(str2)%i:
                return False
            
            m1 = len(str1)//i
            m2 = len(str2)//i
            print(i)
            return m1 * str1[:i] == str1 and m2 * str2[:i] == str2


        for i in range(min(len(str1), len(str2)), 0, -1):
            
            if str1[:i] == str2[:i] and is_divisor(i):
                return str1[:i]
        
        return ""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1

        temp = abs(x)

        rev = 0

        while temp:
            rev = rev * 10 + temp%10
            temp //= 10
        
        rev = rev*sign

        return rev if -pow(2, 31) <= rev <= pow(2, 31)-1 else 0




class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")

        num = 0
        sign = 1
        if not s:
            return 0

        if s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        if not s:
            return num
        
        i = 0
        while i<len(s):
            if not s[i].isdigit():
                break
            num = num*10 + int(s[i])
            i+=1

        left_boundary = -pow(2, 31)
        right_boundary = pow(2, 31)-1

        num = sign*num
        if num < left_boundary:
            return left_boundary
        elif num > right_boundary:
            return right_boundary
        else:
            return num
        

        
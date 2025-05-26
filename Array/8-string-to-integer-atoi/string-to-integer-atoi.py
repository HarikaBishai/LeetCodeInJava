class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")

        if not s:
            return 0

        num = 0
        sign = 1
        

        if s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        if not s:
            return num
        
        for c in s:
            if not c.isdigit():
                break
            num = num*10 + int(c)
           

        left_boundary = -pow(2, 31)
        right_boundary = pow(2, 31)-1

        num = sign*num
        if num < left_boundary:
            return left_boundary
        elif num > right_boundary:
            return right_boundary
        else:
            return num
        

        
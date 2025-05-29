class Solution:
    def calculate(self, s: str) -> int:
        operators = set(["+", "-", "/", "*"])
        stk = []
        curr_num = 0
        opr = '+'
        for i, val in enumerate(s):
            if val.isdigit(): 
                curr_num = curr_num*10 + int(val)
            if val in operators or i == len(s)-1:
                if opr == '+':
                    stk.append(curr_num)
                elif opr == '-':
                    stk.append(-curr_num)
                elif opr == '*':
                    stk[-1] = stk[-1]*curr_num
                elif opr == '/':
                    stk[-1] = int(stk[-1]/curr_num)
                opr = val
                curr_num = 0
        return sum(stk)

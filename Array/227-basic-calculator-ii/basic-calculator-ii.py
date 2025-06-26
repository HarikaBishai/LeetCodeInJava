class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        operators = ['+', '-','/', '*']
        op = '+'
        curr_num = 0
        for i in range(len(s)):
            val = s[i]
            if s[i].isdigit():
                curr_num = curr_num*10+int(val)
            if val in operators or i == len(s)-1:
                if op == '+':
                    stk.append(curr_num)
                elif op == '-':
                    stk.append(-curr_num)
                elif op == '*':
                    stk[-1] = stk[-1]*curr_num
                else:
                    stk[-1] = int(stk[-1]/curr_num)
                op = val
                curr_num = 0
        
        return sum(stk)
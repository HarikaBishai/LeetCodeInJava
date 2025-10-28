class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        for c in s:
            if c == ']':
                curr_s = ''
                while stk and stk[-1]!='[':
                    curr_s = stk.pop() + curr_s
                stk.pop()
                num = ''
                
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(curr_s*int(num))
            else:
                stk.append(c)
        return "".join(stk)
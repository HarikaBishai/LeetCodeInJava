class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        open = close = 0

        stk = []

        def generate(open, close):
            if open == close == n:
                out.append("".join(stk))
                return
            
            if open < n:
                stk.append('(')
                generate(open+1, close)
                stk.pop()
            if close<open:
                stk.append(')')
                generate(open, close+1)
                stk.pop()
        generate(0,0)
        return out
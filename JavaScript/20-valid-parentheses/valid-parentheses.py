class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in '{([':
                stk.append(c)
            elif c in mapping:
                if not stk or mapping[c] != stk.pop():
                    return False
        
        return True if not stk else False
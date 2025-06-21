class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in '({[':
                stk.append(c)
            else:
                if not stk:
                    return False
                top = stk.pop()
                if top != mapping[c]:
                    return False
        return True if not stk else False




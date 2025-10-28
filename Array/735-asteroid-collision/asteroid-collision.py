class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for ast in asteroids:
            
            while stk and ast < 0 and ast!=float('-inf') and stk[-1] > 0:
                top = stk.pop()
                if abs(top) > abs(ast):
                    ast = top
                elif abs(top) == abs(ast):
                    ast = float('-inf')
            
            if ast!=float('-inf'):
                stk.append(ast)
        return stk
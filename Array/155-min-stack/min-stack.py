class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(val)
            self.min_stk.append(val)
            return
        if val < self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])
        self.stk.append(val)

    def pop(self) -> None:
        if not self.stk:
            return -1
        val = self.stk.pop()
        self.min_stk.pop()
        return val

    def top(self) -> int:
        if not self.stk:
            return -1
        return self.stk[-1]


    def getMin(self) -> int:
        if not self.stk:
            return -1
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
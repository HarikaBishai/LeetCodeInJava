from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        if self.q and self.q[-1] == t:
            self.q[-1] = (t, self.q[-1]+1)
        else:
            self.q.append((t,1))
        self.count+=1


        while self.q and self.q[0][0] < t-3000:
            self.count -= self.q.popleft()[1]


        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
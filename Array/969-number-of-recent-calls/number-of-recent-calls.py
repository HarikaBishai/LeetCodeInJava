from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        if self.q and self.q[-1] == t:
            self.q[-1] = (t, self.q[-1]+1)
        else:
            self.q.append((t,1))


        count = 0
        while self.q and self.q[0][0] < t-3000:
            self.q.popleft()

        i = 0
        while i < len(self.q):
            count+= self.q[i][1]
            i+=1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
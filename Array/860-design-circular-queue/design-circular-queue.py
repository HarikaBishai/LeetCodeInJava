class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.count = 0
        self.capacity = k
        self.queue = [None]*k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.head + self.count)%self.capacity] = value
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1)%self.capacity
        self.count-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.head + self.count -1)%self.capacity ]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
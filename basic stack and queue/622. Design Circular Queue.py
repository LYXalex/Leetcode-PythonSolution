class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.maxSize = k
        self.curSize = 0
        self.front = 0
        self.cur = -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.cur = (self.cur + 1) % self.maxSize
            self.queue[self.cur] = value
            self.curSize += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxSize
            self.curSize -= 1
            return True
        return False

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.cur]

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.maxSize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
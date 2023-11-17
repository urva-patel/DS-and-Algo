class MyCircularQueue:

    def __init__(self, k: int):
        self.left = 0
        self.right = 0
        self.arr = [None] * k
        self.size = 0
        self.k = k
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if(self.size == self.k):
            return False
        self.arr[self.right] = value
        self.rear = self.right
        if(self.right == self.k - 1):
            self.right = 0
        else:
            self.right += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if(self.size == 0):
            return False
        self.arr[self.left] = None
        if(self.left == self.k - 1):
            self.left = 0
        else:
            self.left += 1
        self.size -= 1
        return True

    def Front(self) -> int:
        if(self.size == 0):
            return -1
        return self.arr[self.left]

    def Rear(self) -> int:
        if(self.size == 0):
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        if(self.size == 0):
            return True
        return False

    def isFull(self) -> bool:
        if(self.size == self.k):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
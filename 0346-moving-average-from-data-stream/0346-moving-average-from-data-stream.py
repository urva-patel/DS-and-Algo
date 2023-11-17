class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = []
        self.total = 0
        
        

    def next(self, val: int) -> float:
        if len(self.arr) == self.size:
            left = self.arr.pop(0)
            self.total -= left
        self.arr.append(val)
        self.total += val
        return self.total/len(self.arr)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
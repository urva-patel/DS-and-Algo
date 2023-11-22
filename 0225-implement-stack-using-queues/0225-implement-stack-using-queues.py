class MyStack:

    def __init__(self):
        self.qOne = deque()
        self.qTwo = deque()
        

    def push(self, x: int) -> None:
        self.qOne.append(x)
        

    def pop(self) -> int:
        n = len(self.qOne)
        ret = None
        for i in range(n):
            if i == n - 1:
                ret = self.qOne.popleft()
                break
            self.qTwo.append(self.qOne.popleft())
        self.qOne = self.qTwo
        return ret
        

    def top(self) -> int:
        return self.qOne[-1]

    def empty(self) -> bool:
        return len(self.qOne) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
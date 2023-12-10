class TwoSum:

    def __init__(self):
        self.nums = []
        self.sums = set()

    def add(self, number: int) -> None:
        for num in self.nums:
            self.sums.add(number + num)
        self.nums.append(number)

    def find(self, value: int) -> bool:
        if value in self.sums:
            return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
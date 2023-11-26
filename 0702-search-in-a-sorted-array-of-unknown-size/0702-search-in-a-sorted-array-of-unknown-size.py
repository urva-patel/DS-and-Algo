# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10000

        while(left <= right):
            mid = (left + right)//2
            
            if reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if reader.get(left) == target:
            return left
        else:
            return -1

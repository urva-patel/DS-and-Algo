class Solution:
    #once on the target, if finding first true, start cutting of right side aka else has right cut statement, then return left
    #if finding alst true, start cutting left side aka else has the left cut statement then return right
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        def findLeft():
            left, right = 0, len(nums) - 1

            while(left <= right):
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if 0 <= left < len(nums) and nums[left] == target else -1
        
        def findRight():
            left, right = 0, len(nums) - 1

            while(left <= right):
                mid = (left + right)//2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right if 0 <= right < len(nums) and nums[right] == target else -1
        
        left = findLeft()
        right = findRight()

        return [left, right]
        

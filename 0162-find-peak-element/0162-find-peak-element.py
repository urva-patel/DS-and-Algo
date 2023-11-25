class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 0
        left, right = 0, len(nums) - 1

        while(left < right):
            mid = (left + (right - left+1)//2)
            if nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid
        
        return left
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        currSum = 0
        output = math.inf
        while right < len(nums):
            currSum += nums[right]
            right += 1
            while(currSum >= target and left <= right):
                output = min(output, right - left)
                currSum -= nums[left]
                left += 1
        return 0 if output == math.inf else output
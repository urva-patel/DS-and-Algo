class Solution:
    #[7,2,5,10,8]
    def splitArray(self, nums: List[int], k: int) -> int:

        def findWays(mid, nums, k):
            currSum = 0
            count = 0
            for num in nums:
                if currSum + num > mid:
                    count += 1
                    currSum = num
                else:
                    currSum += num
            
            return count + 1

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right)//2

            if findWays(mid, nums, k) > k:
                #need to close off left to increase mid, so array can split less often
                left = mid + 1
            else:
                #need to close off right to decrease mid, since array needs to split more often
                right = mid
        
        return left
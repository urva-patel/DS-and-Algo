class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dp, do memo and go all the way to last number and see if it adds up to 0, if so return true
        memo = {}

        def getTotal(i, rem) -> int:
            if(i == len(nums)):
                if(rem == target):
                    memo[(i, rem)] = 1
                    return 1
                else:
                    memo[(i, rem)] = 0
                    return 0
            
            if (i, rem) in memo:
                return memo[(i, rem)]
            
            pos = getTotal(i + 1, rem + nums[i])
            neg = getTotal(i + 1, rem - nums[i])

            memo[(i, rem)] = pos + neg
            return memo[(i, rem)]

        return getTotal(0, 0)

        
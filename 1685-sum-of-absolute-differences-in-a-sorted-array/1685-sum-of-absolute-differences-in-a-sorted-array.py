class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums) - 1
        # ( curr - (left side sum) ) + ( (right side sum) - curr)
        leftSideSums = [nums[0]]
        rightSideSums = [nums[n]]
        left, right = 1, n - 1
        while right >= 0:
            leftSideSums.append(nums[left] + leftSideSums[left - 1])
            rightSideSums.append(nums[right] + rightSideSums[left - 1])
            left += 1
            right -= 1
        rightSideSums.reverse()

        output.append(rightSideSums[1] - (n)*nums[0] )
        for i in range(1, n):
            rightMult = n - i
            leftMult = i
            leftSum = (leftMult*nums[i] - leftSideSums[i - 1])
            rightSum = (rightSideSums[i + 1] - rightMult*nums[i])
            output.append(leftSum + rightSum)
        output.append(nums[n]*(n) - leftSideSums[n - 1])

        return output


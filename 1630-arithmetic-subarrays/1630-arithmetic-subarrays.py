class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            subArr = nums[l[i]:r[i] + 1]
            subArr.sort()
            diff = subArr[1] - subArr[0]
            flag = True
            for j in range(1, len(subArr)):
                compare = subArr[j] - subArr[j - 1]
                if(compare != diff):
                    flag = False
                    break
            output.append(flag)
        
        return output

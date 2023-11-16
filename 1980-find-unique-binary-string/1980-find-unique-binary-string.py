class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            #get ith char of the ith binary string
            curr_char = nums[i][i]
            result.append('1' if curr_char == "0" else "0")
        
        return "".join(result)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputDict = {}
        for myStr in strs:
            sortedStr = ''.join(sorted(myStr))
            if sortedStr in outputDict:
                outputDict[sortedStr].append(myStr)
            else:
                outputDict[sortedStr] = [myStr]
        
        output = []
        for arr in outputDict.values():
            output.append(arr)
        
        return output
        
        
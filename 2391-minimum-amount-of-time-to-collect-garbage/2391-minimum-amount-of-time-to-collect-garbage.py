class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefixSum = [0]
        for num in travel:
            prefixSum.append(prefixSum[-1] + num)
        
        types = {}
        for i, letters in enumerate(garbage):
            for letter in letters:
                types[letter] = prefixSum[i]
        
        g = sum(map(len, garbage))
        return sum(types.values()) + g
        
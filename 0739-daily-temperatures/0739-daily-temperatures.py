class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while(stack and v > stack[-1][0]):
                old = stack.pop()
                out[old[1]] = i - old[1]
            stack.append([v, i])
        
        return out


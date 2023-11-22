class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = 0
        output = ""
        for c in s:
            if c == '[':
                stack.append(output)
                stack.append(curr)
                curr = 0
                output = ""
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                output = prevString + num*output
            elif c.isdigit():
                curr = curr*10 + int(c)
            else:
                output += c
        
        return output
            
            
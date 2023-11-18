class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '{', '[']
        openSet = set(opens)
        stack = []
        for p in s:
            if p in openSet:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                potOpen = stack.pop()
                if p == ')' and potOpen != '(':
                    return False
                if p == ']' and potOpen != '[':
                    return False
                if p == '}' and potOpen != '{':
                    return False
        if len(stack) > 0:
            return False
        return True
                
                    
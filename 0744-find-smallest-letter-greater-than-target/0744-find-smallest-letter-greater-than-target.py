class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        lexTarget = target

        while left < right:
            mid = (left + right)//2
            lexMid = letters[mid]

            if lexMid <= lexTarget:
                left = mid + 1
            else:
                right = mid
        
        if letters[left] > lexTarget:
            return letters[left]
        else:
            return letters[0]
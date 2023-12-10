class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        output = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

            seen.add(s[right])
            counter = right - left + 1
            output = max(output, counter)
        
        return output
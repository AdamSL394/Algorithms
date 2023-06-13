class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        A = 0
        seen = set()
        count = 0 
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[A])
                A += 1
            seen.add(s[r])
            count = max(count, r - A +  1)
            
        return count
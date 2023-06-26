class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        a = 0
        for letter in range(len(s)):
            while s[letter] in seen:
                seen.remove(s[a])
                a += 1
            seen.add(s[letter])
            res = max(res, len(seen))
        return res
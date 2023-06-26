class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        l,r = 0 , 0
        
        for letter in range(len(s)):
            l,r = letter , letter
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
            l,r = letter , letter + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1)  > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
    
        return res
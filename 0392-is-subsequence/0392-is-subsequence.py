class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        a = 0
        for letter in t:
            if a == len(s):
                return True
            if letter == s[a]:
                a += 1

        return True if (a) == len(s) else False

        
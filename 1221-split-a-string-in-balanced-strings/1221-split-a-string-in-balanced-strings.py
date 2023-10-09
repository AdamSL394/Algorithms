class Solution:
    def balancedStringSplit(self, s: str) -> int:
        N = len(s)
        L, R = int(N / 2),  int(N / 2)
        res = 0
        
        for v in range(N):
            if L == R:
                res += 1
            if s[v] == "L":
                L -= 1
            if s[v] == "R":
                R -= 1
                
        return res
            
            
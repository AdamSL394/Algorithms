class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        
        def recusive(n):
            if n == 1:
                return 1
            if n == 2: 
                return 2
            if n == 3:
                return 3
            
            if n in dp:
                return dp[n]
            
            dp[n] = recusive(n - 1) + recusive(n - 2)
            return dp[n]
        return recusive(n)
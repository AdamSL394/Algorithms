class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        N = len(fruits)
        l = 0
        Inf = -10**5
        best = Inf
        count = {}

        
        for r in range(N):
            if fruits[r] in count:
                count[fruits[r]] += 1
            else:
                count[fruits[r]] = 1
            
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            best = max(best, (r-l) + 1)
            
            
        return (best)
                
            
            
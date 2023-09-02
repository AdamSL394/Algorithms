"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        x = 1
        cache = {}
        res = []
        
        def test_function(x, y):
            if x > z:
                return
            
            if (x, y) in cache:
                return cache[(x, y)]
            
            for y in range(1, z + 1):
                if customfunction.f(x, y) == z:
                    cache[(x,y)] = True
                else:
                    customfunction.f(x, y)
                    cache[(x,y)] = False
                test_function(x + 1, y)
            return cache

        test = (test_function(x, 1))
        
        for k,v in test.items():
            if v == True:
                res.append(list(k))
        return res        
        
        
        """
       0 , 0 
        
        """
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool: 
        if n < 1:
            return False

        return(math.log2(n).is_integer())
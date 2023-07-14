import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        N = len(flowerbed) - 1
        count = 0
        
        for i in range(1, N):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
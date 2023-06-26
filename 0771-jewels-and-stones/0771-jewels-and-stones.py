class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        rare = set(jewels)
        
        count = 0
        
        for letter in stones:
            if letter in rare:
                count += 1
        return count
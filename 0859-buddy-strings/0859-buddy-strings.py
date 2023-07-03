class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        N = len(s)
        
        diff = 0
        for i in range(N):
            if s[i] != goal[i]:
                diff += 1 
        print(diff)
        if diff > 2:
            return False
        
        if diff == 1:
            return False
        
        if diff == 0:
            return max(collections.Counter(s).values()) >= 2
        
        return collections.Counter(s) ==  collections.Counter(goal)
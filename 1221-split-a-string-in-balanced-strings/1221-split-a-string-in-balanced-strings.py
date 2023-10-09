class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        R:5, 4, 3, 2
        L:5, 4, 3, 2


        "RLRRLLRLRL"
               ^
        0, 1, 2
        """
        l_r_counter = Counter(s)

        N = len(s)
        res = 0
        
        for v in range(N):
            if l_r_counter["L"] == l_r_counter["R"]:
                res += 1
            if s[v] == "L":
                l_r_counter["L"] -= 1
            if s[v] == "R":
                l_r_counter["R"] -= 1
                
        return res
            
            
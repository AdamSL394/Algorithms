class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        
        """
        res = [2,4,1,2,5]
        
        [
         [1,1,0,0,0],
         [1,1,1,1,0],
         [1,0,0,0,0],
         [1,1,0,0,0],
         [1,1,1,1,1]
        ], 
        
        """
        
        rank = []
        res = []
        
        row = len(mat)
        col = len(mat[0])
        
        for i in range(row):
            score = 0
            for j in range(col):
                if mat[i][j] == 1:
                    score += 1
            rank.append((score, i))
            score = 0
        i = 0
        classify = sorted(rank)
        
        for t,v in classify:
            if k == 0:
                return res
            res.append(v)
            k -= 1
        return res
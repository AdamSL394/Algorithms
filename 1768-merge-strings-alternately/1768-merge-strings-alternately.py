class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
       
        word_turn = word1
        l = 0 
        r = 0
        
        while l < len(word1) and r < len(word2):
            if word_turn == word1 and l < len(word1):
                res.append(word1[l])
                word_turn = word2
                l += 1
            if word_turn == word2 and r < len(word2):
                res.append(word2[r])
                word_turn = word1
                r += 1
                
        if l < len(word1):
            res.append(word1[l:])
        if r < len(word2):
            res.append(word2[r:])
            
        return ''.join(res)
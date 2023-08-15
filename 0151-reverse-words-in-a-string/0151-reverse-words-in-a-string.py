class Solution:
    def reverseWords(self, s: str) -> str:
        

        li = list(s.split())
        
        res = []
        
        for x in range(len(li) -1 ,-1,-1):
            res.append(li[x])
            
        return ' '.join(res)
        
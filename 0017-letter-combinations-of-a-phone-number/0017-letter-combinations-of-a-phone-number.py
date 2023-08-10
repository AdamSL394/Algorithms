class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        phone = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        
        res = []
        
        
        def helper(i,c):
            if len(c) == len(digits):
                res.append("".join(c))
                return
            
            
            for v in phone[digits[i]]:
                c.append(v)
                helper(i + 1, c)
                c.pop()
        
        if digits:
            helper(0,[])
            
        return res   
        
        
        
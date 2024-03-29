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
        
        
        def combos(i,s):
            if len(s) == len(digits):
                res.append(s)
                return
            
            for v in phone[digits[i]]:
                combos(i + 1, s = s + v)
            
        
        combos(0,'')
        return res
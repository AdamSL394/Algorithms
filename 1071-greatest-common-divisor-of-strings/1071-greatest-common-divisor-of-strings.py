class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1) , len(str2)

        
        def helper(word):
            if l1 % word != 0 or l2 % word != 0:
                return False
            f1, f2 = l1 // word, l2 // word
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2 
        for l in range(min(l1,l2),0,-1):
            if helper(l):
                return str1[:l]
        return ""
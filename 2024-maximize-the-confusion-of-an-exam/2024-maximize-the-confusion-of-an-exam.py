class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        T = 0
        F = 0 
        
        l = 0
        given = k
        Inf = -10**4
        res = Inf
        
        for r in range(N):
            if answerKey[r] == "F":
                F += 1
            if answerKey[r] == "T":
                T += 1

            while min(T, F)> given:
                if answerKey[l] == "F":
                    F -= 1
                if answerKey[l] == "T":
                    T -= 1
                l += 1

            res = max(res, (r - l)  + 1)
        return res
        

            
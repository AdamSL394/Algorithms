class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = [] #bacd
        reverse = [] # ab, 
        
        limit = k
        N = len(s)
        flag = False
        
        for i in range(N):
            if flag:
                if limit < k:
                    res.append(s[i])
                    limit += 1
                if limit == k:
                    flag = False
                    continue
            if not flag:
                if limit > 0:
                    reverse.append(s[i])
                    limit -= 1

                if limit == 0:
                    res.append(''.join(reverse[::-1]))
                    reverse = []
                    flag = True
        
        if len(reverse) > 0:
            res.append(''.join(reverse[::-1]))
            
        return ''.join(res)
 
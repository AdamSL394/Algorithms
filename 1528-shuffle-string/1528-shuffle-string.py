class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ' ' * len(s)
        ans = list(res)
              
        for i in range(len(indices)):
            ans[indices[i]] = s[i]
            
        return ''.join(ans)
            
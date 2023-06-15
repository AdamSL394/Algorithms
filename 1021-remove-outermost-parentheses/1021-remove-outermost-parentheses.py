class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level = 0
        
        result = []
        
        for i in s:
            if i =="(":
                if level != 0:
                    result.append(i)
                level += 1
            else:
                if level != 1:
                    result.append(i)
                level -=1
        return ''.join(result)
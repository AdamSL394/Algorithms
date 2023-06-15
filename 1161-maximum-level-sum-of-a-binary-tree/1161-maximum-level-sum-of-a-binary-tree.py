# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = [root] 
        
        total =  float('-inf')
        level = 0
        i = 0
        
        while q:
            i += 1
            currentLevelVal = 0
            for node in range(len(q)):
                curr = q.pop(0)
                currentLevelVal += curr.val
                if curr.left:
                    q.append(curr.left)
            
                if curr.right:
                    q.append(curr.right)
                    
            if currentLevelVal > total:
                total = currentLevelVal
                level = i
            
        return level
            
                
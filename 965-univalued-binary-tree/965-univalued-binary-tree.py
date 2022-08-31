# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        pastvalue = root.val
        def dfs(node):
            if not node:
                return True
            
            if node.val != pastvalue:
                return False

            res = dfs(node.left)
            ans = dfs(node.right)
            print(res,ans)
            if ans and res:
                return True
            else:
                return False
            
            if node.val == pastvalue:
                return True
            
            
        
        return dfs(root)
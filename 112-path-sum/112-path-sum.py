# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        target = targetSum
        
        def dfs(node,currentSum):
            if not node:
                return False
            
            if not node.left and not node.right:
                target = currentSum + node.val
                if target == targetSum:
                    return True
            
            return (dfs(node.left,currentSum + node.val) or dfs(node.right,currentSum + node.val))
            
        
            
        return dfs(root,0)
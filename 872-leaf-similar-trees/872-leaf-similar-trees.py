# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        root_one_leaves = []
        root_two_leaves = []
        def dfs(node):
            if not node:
                return
            
            if not node.left and not node.right:
                root_one_leaves.append(node.val)
                
            dfs(node.left)
            dfs(node.right)
        dfs(root1)
            
        def dfss(node):
            if not node:
                return
            
            if not node.left and not node.right:
                root_two_leaves.append(node.val)
                
            dfss(node.left)
            dfss(node.right)
        

        dfss(root2)
        if root_one_leaves != root_two_leaves:
            return False
        else:
            return True
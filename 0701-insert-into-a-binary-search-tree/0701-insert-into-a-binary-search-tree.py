# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return  TreeNode(val)
        
        def dfs(node):
            if node is None:
                newNode = TreeNode(val)
                return newNode
            
            left = None
            right = None
            
            if val < node.val:
                left = dfs(node.left)
            else :
                right = dfs(node.right)
                
                
            if left:
                node.left = left
            if right:
                node.right = right
            
            return None
            
            
        dfs(root)
        
        return root
        
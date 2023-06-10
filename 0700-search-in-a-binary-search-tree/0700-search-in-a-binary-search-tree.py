# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def traverse(node):
            if not node:
                return
            
            if node.val == val:
                return node

            return traverse(node.left) or traverse(node.right)
            
        return traverse(root)
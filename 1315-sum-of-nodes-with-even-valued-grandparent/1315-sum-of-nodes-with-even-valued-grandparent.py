# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def traverse(node, parent, grandparent):
            
            if not node:
                return
            
            if grandparent is not None and grandparent.val % 2 == 0:
                self.res += node.val
            
            traverse(node.left, node, parent)
            traverse(node.right, node, parent)
            
            return self.res
        
        
        return traverse(root, None, None)
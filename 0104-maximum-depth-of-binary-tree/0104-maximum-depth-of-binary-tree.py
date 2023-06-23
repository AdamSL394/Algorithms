# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        stack = [root]
        level = 0
        increment = False
        
        while stack: 
            level += 1
            for node in range(len(stack)):
                value = stack.pop(0)
                if value:
                    if value.left:
                        stack.append(value.left)
                    if value.right:
                        stack.append(value.right)
            
        return level
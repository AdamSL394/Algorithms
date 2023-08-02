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
        
        level = 0
        stack = [root] # 9, 20
        
        while stack:
            level += 1
            for node in range(len(stack)):
                curr = stack.pop(0)
                
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            
        return level
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        diff = set() # 4 , #6
        
        q = [root] # 3 , 6

        
        while q:
            
            node = q.pop(0)
            
            total = k - node.val 

            if node.val in diff:
                return True

            diff.add(total)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return False
        
        
        
        
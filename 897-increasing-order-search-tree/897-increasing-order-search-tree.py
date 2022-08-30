# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        orderedArray = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            orderedArray.append(root.val)
            helper(root.right)
        helper(root)
        
        newRoot = TreeNode(orderedArray[0])
        
        currentNode = newRoot
        for v in orderedArray[1:]:
            node = TreeNode(v)
            currentNode.right = node
            currentNode.left = None
            currentNode = node
        return(newRoot)
            
            
        
            
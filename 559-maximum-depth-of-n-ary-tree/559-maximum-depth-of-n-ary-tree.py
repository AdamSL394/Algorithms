"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: 
            return 0
        depth = 0 
        q = [root]
        while len(q) > 0:
            for node in range(len(q)):
                curr = q.pop(0)
                for v in curr.children:
                    q.append(v)
            depth += 1
        return(depth)
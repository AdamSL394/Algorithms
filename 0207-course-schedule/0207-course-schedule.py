class Projects:
    def __init__(self, val):
        self.val = val
        self.status = ['Pending', 'Complete', 'Blank']
        self.stats = 'Blank'

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        if not prerequisites:
            return True
        dic = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            dic[crs].append(pre)
#         dic = {}
        
#         for a , b in prerequisites:
#             if a not in dic:
#                 dic[a] = []
#             dic[a].append(b)
#             if b not in dic:    
#                 dic[b] = []
        
        seen = set() 
        
        def dfs(node):
            if node in seen:
                return False
            if dic[node] == []:
                return True
            seen.add(node)
            
            for nodes in dic[node]:
                if not dfs(nodes): return False
            seen.remove(node)
            dic[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            

    
            
    
    
class Projects:
    def __init__(self, val):
        self.val = val
        self.status = ['Pending', 'Complete', 'Blank']
        self.stats = 'Blank'

class Solution:
    

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        aL = {}
        seen = set()

        if len(prerequisites) == 0:
            return True

        for classes in prerequisites:
            if classes[0] not in aL:
                aL[classes[0]] = []
            aL[classes[0]].append(classes[1])


        def dfs(proj):
            if proj in seen:
                return False
            if proj not in aL:
                return True
            if aL[proj] == []:
                return True
        
            seen.add(proj)
            children = aL[proj]

            for child in children:
                if dfs(child) == False:
                    return False
            seen.remove(proj)
            aL[proj] = []
            return True
        
        for curriculum in prerequisites:
            projects = curriculum[0]
            if not dfs(projects): return False
        return True
    
            
    
    
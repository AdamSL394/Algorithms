class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        N = len(rooms)
        hasAccess = [False for _ in range(N)]
        hasAccess[0] = True
        
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
        
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
                    
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
        
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
                    
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
        
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
        
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
                    
        for room in range(N):
            for key in rooms[room]:
                if hasAccess[room]:
                    hasAccess[key] = True
                    
        return all(hasAccess)
            
            
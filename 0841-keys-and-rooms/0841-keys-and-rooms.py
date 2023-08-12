class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        N = len(rooms)
        hasAccess = [False for _ in range(N)]
        hasAccess[0] = True
        seen = set()
        stack = [0]
        
        while stack:
            nei = stack.pop(0)
            seen.add(nei)
            for node in rooms[nei]:
                if node not in seen:
                    stack.append(node)
                    hasAccess[node] = True
                    
        return all(hasAccess)
            
            